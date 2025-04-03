import builtins
import threading
import time
import sys
import requests
import aiohttp
import io
import shutil
from collections import deque
from .styles import bar_styles, style_text, check_bar_style_syntax
from .patches import (
    PatchedFile,
    PatchedResponse,
    PatchedAIOHTTPResponse,
    patch_aiohttp_request,
)
_patches = (
    PatchedFile,
    PatchedResponse,
    PatchedAIOHTTPResponse,

)



class SmartBar:
    _instances = []
    _io_patched = False
    _global_lock = threading.Lock()
    _position_map = {}

    def __init__(
        self,
        desc: str,
        length: int = 40,
        stream=sys.stdout,
        position: str = "/r",
        style: str = r"#.", # "——", "||", "==", "##", "==", "~~", r"#.", r"~.", r"~#"
        bar_style: str = "normal",
        auto_bar: bool = True,
        mode: str = "bytes",
        unit: str = None,
        custom_bar_output: str = None,
        custom_bar_style: dict = None,
    ):
        self.desc = desc
        self.length = length
        self.stream = stream
        self.total = 0
        self.current = 0
        self.position = position
        self._start_time = None
        self._speed_window = deque(maxlen=5)
        self._running = False
        self._paused = False
        self._lock = threading.Lock()
        self._thread = None
        self._auto_total_set = False
        self.style = style
        self.auto_bar = auto_bar
        self.mode = mode
        self.unit = unit
        self.custom_bar_output = custom_bar_output
        self.bar_styles = bar_styles
        self.bar_style = bar_style
        self.custom_bar_style = custom_bar_style


        if self.custom_bar_style:
            check_bar_style_syntax(self.custom_bar_style)
            self.bar_style = "custom"
            self.bar_styles["custom"] = self.custom_bar_style

        if self.bar_style not in self.bar_styles:
            raise ValueError(f"Invalid bar style: {self.bar_style}\nall Styles: {list(self.bar_styles.keys())}")
        
        self._bar_style = self.bar_styles[self.bar_style]
        

        if self.mode == "custom" and not self.unit:
            raise ValueError("Custom mode requires a 'unit' argument.")
        if self.position not in ["top", "bottom", "/r"]:
            raise ValueError("Position must be 'top', 'bottom', or '/r'.")
        if self.mode not in ["bytes", "steps", "items", "custom"]:
            raise ValueError("Mode must be 'bytes', 'steps', 'items', or 'custom'.")

    def __enter__(self):
        with SmartBar._global_lock:
            self._nested_level = len(SmartBar._instances)
            SmartBar._instances.append(self)
            self._assign_position()
            if self.auto_bar and not SmartBar._io_patched:
                self._patch_io()
                SmartBar._io_patched = True

        self._start_time = time.time()
        self._running = True
        self._paused = False
        self._thread = threading.Thread(target=self._refresh_loop, daemon=True)
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._running = False
        if self._thread:
            self._thread.join()

        with SmartBar._global_lock:
            if self in SmartBar._instances:
                SmartBar._instances.remove(self)
            SmartBar._position_map.pop(self, None)
            if self.auto_bar and not SmartBar._instances:
                self._restore_io()
                SmartBar._io_patched = False

        self.stream.write("\n")
        self.stream.flush()

    async def __aenter__(self):
        return self.__enter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.__exit__(exc_type, exc_val, exc_tb)

    def _assign_position(self):
        lines = shutil.get_terminal_size().lines
        used_top = [SmartBar._position_map[b] for b in SmartBar._instances if b.position == "top"]
        used_bottom = [SmartBar._position_map[b] for b in SmartBar._instances if b.position == "bottom"]

        if self.position == "top":
            pos = 0
            while pos in used_top:
                pos += 1
            SmartBar._position_map[self] = pos
        elif self.position == "bottom":
            pos = lines - 1
            while pos in used_bottom:
                pos -= 1
            SmartBar._position_map[self] = pos
        else:
            SmartBar._position_map[self] = -1

    def _patch_io(self):
        self._orig_open = builtins.open
        builtins.open = self._patched_open

        self._orig_requests_get = requests.get
        requests.get = self._patched_requests_get

        self._orig_aiohttp_session = aiohttp.ClientSession._request
        patch_aiohttp_request()


    def _restore_io(self):
        builtins.open = self._orig_open
        requests.get = self._orig_requests_get
        aiohttp.ClientSession._request = self._orig_aiohttp_session

        

    def _patched_open(self, *args, **kwargs):
        f = self._orig_open(*args, **kwargs)
        return PatchedFile(f)

    def _patched_requests_get(self, *args, **kwargs):
        resp = self._orig_requests_get(*args, **kwargs)
        try:
            transfer_encoding = resp.headers.get("Transfer-Encoding", "").lower()
            if "chunked" in transfer_encoding:
                self.total = 0
            else:
                length = int(resp.headers.get("Content-Length", 0))
                if length and not self._auto_total_set:
                    self.total = length
                    self._auto_total_set = True
        except:
            pass
        return PatchedResponse(resp)
    

    def _refresh_loop(self):
        last_bytes = 0
        last_time = time.time()
        while self._running:
            if self._paused:
                time.sleep(0.1)
                continue

            now = time.time()
            elapsed = now - last_time
            if elapsed > 0.1:
                delta = self.current - last_bytes
                speed = delta / elapsed if elapsed > 0 else 0
                self._speed_window.append(speed)
                last_bytes = self.current
                last_time = now
            self._redraw_all()
            time.sleep(0.1)

    @classmethod
    def _redraw_all(cls):
        with cls._global_lock:
            for bar in sorted(cls._instances, key=lambda b: b._nested_level):
                stream = bar.stream

                stream.write("\0337")         
                stream.write("\033[?25l")     

                line = cls._position_map.get(bar, -1)
                if line >= 0:
                    stream.write(f"\033[{line + 1};0H")

                bar._draw(inline=(line == -1))

                stream.write("\0338")         
                stream.flush()

    def fmt_value(self, value):
        if self.mode == "bytes":
            for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                if value < 1024:
                    return f"{value:.1f} {unit}"
                value /= 1024
            return f"{value:.1f} PB"
        elif self.mode in ("steps", "items", "custom"):
            return f"{value:.1f} {self.unit or ''}"
        return str(value)

    def _draw(self, inline=False):
        with self._lock:
            percent = self.current / self.total if self.total else 0
            percent = min(percent, 1.0)
            filled = int(self.length * percent)

            
            bar = ""
            bar_filled_char, bar_unfilled_char = self.style[0], self.style[1]
            bar_colors = self._bar_style["BAR"]

            fg_fill, bg_fill = bar_colors.get("+", [None, None])
            fg_unfill, bg_unfill = bar_colors.get("-", [None, None])

            for i in range(self.length):
                if i < filled:
                    bar += style_text(bar_filled_char, [fg_fill, bg_fill])
                else:
                    bar += style_text(bar_unfilled_char, [fg_unfill, bg_unfill])

            
            speed = sum(self._speed_window) / len(self._speed_window) if self._speed_window else 0
            window_speed = speed
            avg_speed = self.current / (time.time() - self._start_time + 1e-6)
            combined_speed = (0.7 * window_speed + 0.3 * avg_speed)
            eta = (self.total - self.current) / combined_speed if self.total and combined_speed else None

          
            cur_disp = self.fmt_value(self.current)
            total_disp = self.fmt_value(self.total) if self.total else "?"
            speed_disp = self.fmt_value(combined_speed) + "/s" if combined_speed else "-"
            eta_disp = f"{eta:.1f}s" if eta is not None and eta >= 0 else "?"

        
            DESC_C = self._bar_style["DESC"]
            CUR_C = self._bar_style["CUR"]
            TOTAL_C = self._bar_style["TOTAL"]
            PERCENT_C = self._bar_style["PERCENT"]
            SPEED_C = self._bar_style["SPEED"]
            ETA_C = self._bar_style["ETA"]

            desc_disp = style_text(self.desc, DESC_C)
            cur_disp = style_text(cur_disp, CUR_C)
            total_disp = style_text(total_disp, TOTAL_C)
            percent_disp = style_text(f"{percent * 100:.1f}%", PERCENT_C)
            speed_disp = style_text(speed_disp, SPEED_C)
            eta_disp = style_text(eta_disp, ETA_C)

            if self.custom_bar_output:
                output = self.custom_bar_output
                output = output.replace("%(DESC)", desc_disp)
                output = output.replace("%(BAR)", bar)
                output = output.replace("%(CUR)", cur_disp)
                output = output.replace("%(TOTAL)", total_disp)
                output = output.replace("%(PERCENT)", percent_disp)
                output = output.replace("%(SPEED)", speed_disp)
                output = output.replace("%(ETA)", eta_disp)
            else:
                output = (
                    f"{desc_disp:20} [{bar}] {cur_disp}/{total_disp} "
                    f"({percent_disp}) | {speed_disp} | ETA: {eta_disp}"
                )

            if inline:
                self.stream.write("\r\033[2K")
                self.stream.write(output)
                self.stream.write(" " * 10 + "\r")
            else:
                self.stream.write("\033[2K")
                self.stream.write(output + "\n")

            self.stream.flush()

    def pause(self):
        with self._lock:
            self._paused = True

    def resume(self):
        with self._lock:
            if not self._running:
                return
            self._paused = False

    def update(self, value):
        with self._lock:
            self.current = value
            if self.total and self.current > self.total:
                self.current = self.total

    def add(self, n):
        with self._lock:
            self.current += n
            if self.total and self.current > self.total:
                self.current = self.total

    @classmethod
    def ignore(cls, obj):
        if isinstance(obj, _patches):
            obj._ignore = True

    @classmethod
    def unignore(cls, obj):
        if isinstance(obj, _patches):
            obj._ignore = False
    
    def track(self, obj):
        
        if isinstance(obj, _patches):
            return obj

        
        if isinstance(obj, io.IOBase):
            orig_write = obj.write if hasattr(obj, "write") else None
            orig_read = obj.read if hasattr(obj, "read") else None

            def new_write(data):
                result = orig_write(data)
                self.add(len(data))
                return result

            def new_read(size=-1):
                data = orig_read(size)
                self.add(len(data))
                return data

            if orig_write:
                obj.write = new_write
            if orig_read:
                obj.read = new_read
            return obj

        
        return obj