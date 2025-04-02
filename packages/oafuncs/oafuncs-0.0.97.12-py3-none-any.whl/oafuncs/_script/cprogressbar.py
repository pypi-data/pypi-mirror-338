# progressbar.py
import sys
import shutil
import time
import warnings
from typing import Iterable, Any, List, Union
import numpy as np

try:
    from matplotlib.colors import LinearSegmentedColormap, to_rgb, to_hex
    from matplotlib.cm import get_cmap
except ImportError:
    raise ImportError("This module requires matplotlib. Install with: pip install matplotlib")


class ColorProgressBar:
    def __init__(self, iterable: Iterable, prefix: str = "", color: Any = "cyan", cmap: Union[str, List[str]] = None, update_interval: float = 0.1, bar_length: int = None):
        self.iterable = iterable
        self.prefix = prefix
        self.base_color = color
        self.cmap = cmap
        self.update_interval = update_interval
        self.bar_length = bar_length

        self._start_time = None
        self._last_update = 0
        self._count = len(iterable) if hasattr(iterable, "__len__") else None
        self._file = sys.stdout
        self._gradient_colors = self._generate_gradient() if cmap else None

    def _generate_gradient(self) -> List[str]:
        """生成渐变色列表（修复内置colormap支持）"""
        try:
            if isinstance(self.cmap, list):
                cmap = LinearSegmentedColormap.from_list("custom_cmap", self.cmap)
            else:
                # 正确获取Matplotlib内置colormap
                cmap = get_cmap(self.cmap)

            return [to_hex(cmap(i)) for i in np.linspace(0, 1, self._count)]
        except Exception as e:
            warnings.warn(f"Colormap generation failed: {str(e)}")
            return None

    def _hex_to_ansi(self, hex_color: str) -> str:
        """将颜色转换为ANSI真彩色代码"""
        try:
            rgb = [int(x * 255) for x in to_rgb(hex_color)]
            return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
        except ValueError as e:
            warnings.warn(f"Invalid color value: {e}, falling back to cyan")
            return "\033[96m"

    def _resolve_color(self, index: int) -> str:
        """解析当前应使用的颜色"""
        if self._gradient_colors and index < len(self._gradient_colors):
            try:
                return self._hex_to_ansi(self._gradient_colors[index])
            except IndexError:
                pass

        return self._process_color_value(self.base_color)

    def _process_color_value(self, color: Any) -> str:
        """处理颜色输入格式"""
        preset_map = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "cyan": "\033[96m",
        }

        if color in preset_map:
            return preset_map[color]

        try:
            hex_color = to_hex(color)
            return self._hex_to_ansi(hex_color)
        except (ValueError, TypeError) as e:
            warnings.warn(f"Color parsing failed: {e}, using cyan")
            return preset_map["cyan"]

    def _format_bar(self, progress: float, width: int) -> str:
        """格式化进度条显示"""
        filled = "▊"
        empty = " "
        max_width = width - 50
        filled_length = int(round(max_width * progress))
        return filled * filled_length + empty * (max_width - filled_length)

    def _calculate_speed(self, index: int, elapsed: float) -> tuple:
        """计算速率和剩余时间"""
        if index == 0 or elapsed < 1e-6:
            return 0.0, 0.0

        rate = index / elapsed
        remaining = (self._count - index) / rate if self._count else 0
        return rate, remaining

    def __iter__(self):
        self._start_time = time.time()
        self._last_update = self._start_time
        reset_code = "\033[0m"

        for i, item in enumerate(self.iterable):
            now = time.time()
            elapsed = now - self._start_time
            yield item

            if (now - self._last_update) < self.update_interval and i + 1 != self._count:
                continue

            term_width = self.bar_length or shutil.get_terminal_size().columns
            progress = (i + 1) / self._count if self._count else 0

            current_color = self._resolve_color(i) if self._gradient_colors else self._resolve_color(0)

            bar = self._format_bar(progress, term_width)
            rate, remaining = self._calculate_speed(i + 1, elapsed)

            count_info = f"{i + 1}/{self._count}" if self._count else str(i + 1)
            percent = f"{progress:.1%}" if self._count else ""
            rate_info = f"{rate:.1f}it/s" if rate else ""
            time_info = f"ETA: {remaining:.1f}s" if self._count else f"Elapsed: {elapsed:.1f}s"

            line = (f"\r{self.prefix}{current_color}[{bar}]{reset_code} {count_info} {percent} [{time_info} | {rate_info}]").ljust(term_width)

            self._file.write(line)
            self._file.flush()
            self._last_update = now

        self._file.write("\n")
        self._file.flush()

    @classmethod
    def gradient_color(cls, colors: List[str], n: int) -> List[str]:
        """生成渐变色列表"""
        cmap = LinearSegmentedColormap.from_list("gradient", colors)
        return [to_hex(cmap(i)) for i in np.linspace(0, 1, n)]


# 验证示例
if __name__ == "__main__":
    # 正确使用内置colormap
    for _ in ColorProgressBar(range(100), cmap="viridis", prefix="Viridis: "):
        time.sleep(0.05)

    # 使用自定义渐变色
    for _ in ColorProgressBar(range(50), cmap=["#FF0000", "#0000FF"], prefix="Custom: "):
        time.sleep(0.1)
