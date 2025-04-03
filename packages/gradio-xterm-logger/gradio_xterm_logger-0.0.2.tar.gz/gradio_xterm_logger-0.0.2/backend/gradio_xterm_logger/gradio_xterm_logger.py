from __future__ import annotations
import os
import sys
import tempfile
from collections import deque
from typing import Any, Callable, TYPE_CHECKING, TextIO, Deque
from gradio.components.base import Component

if TYPE_CHECKING:
    from gradio.components import Timer
    from typing import TextIO

class GradioXtermLogger(Component):
    __redirected: bool = False  # Class-level flag to track redirection
    
    def __init__(
        self, 
        log_path: str | None = None,
        dark_mode: bool = True,
        font_size: int = 12,
        show_current_terminal: bool = False,
        n_lines: int = 40,
        label: str | None = None, 
        info: str | None = None,
        show_label: bool | None = None,
        container: bool = True,
        scale: int | None = None,
        min_width: int | None = None,
        interactive: bool | None = None,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        load_fn: Callable[..., Any] | None = None,
        every: float | None = 0.5
    ):
        
        self.user_log_path: str | None = log_path
        self.log_path: str = log_path or self._create_temp_log()
        self.show_current_terminal: bool = show_current_terminal
        self.n_lines: int = n_lines
        self.dark_mode: bool = dark_mode
        self.font_size: int = font_size
        
        if self.show_current_terminal and not GradioXtermLogger.__redirected:
            self._redirect_terminal_output()
            GradioXtermLogger.__redirected = True

        super().__init__(
            value=self._update_terminal, 
            label=label,
            info=info,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            interactive=interactive,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
            load_fn=load_fn,
            every=every
        )
    
    def _create_temp_log(self) -> str:
        fd: int
        path: str
        fd, path = tempfile.mkstemp(
            prefix="gradio_terminal_",
            suffix=".log",
            dir=os.getenv('TMPDIR', '/tmp')
        )
        os.close(fd)
        return path

    def _redirect_terminal_output(self) -> None:
        """Redirect stdout/stderr only if not already redirected"""

        class DualWriter:
            def __init__(self, terminal: TextIO, log_file: TextIO):
                self.terminal: TextIO = terminal
                self.log_file: TextIO = log_file

            def write(self, message: str) -> None:
                self.terminal.write(message)
                self.log_file.write(message)
                self.log_file.flush()

            def flush(self) -> None:
                self.terminal.flush()
                self.log_file.flush()

            def isatty(self) -> bool:
                return self.terminal.isatty()

            def fileno(self) -> int:
                return self.terminal.fileno()

        if isinstance(sys.stdout, DualWriter):
            return  # Already redirected
        
        self.log_file: TextIO = open(self.log_path, "a")
        sys.stdout = DualWriter(sys.stdout, self.log_file)  # type: ignore
        sys.stderr = DualWriter(sys.stderr, self.log_file)  # type: ignore

    def _update_terminal(self) -> list[str]:
        if not os.path.exists(self.log_path):
            return []

        try:
            with open(self.log_path, 'r') as log:
                maxlen: int | None = self.n_lines if self.n_lines > 0 else None
                lines: Deque[str] = deque(log, maxlen=maxlen)
                return [line.rstrip('\n') for line in lines]
        except Exception as e:
            return []

    def preprocess(self, payload: Any) -> Any:
        return payload

    def postprocess(self, value: Any) -> Any:
        return value

    def example_payload(self) -> dict[str, str]:
        return {"foo": "bar"}

    def example_value(self) -> dict[str, str]:
        return {"foo": "bar"}

    def api_info(self) -> dict[str, Any]:
        return {"type": {}, "description": "any valid json"}

    def get_config(self) -> dict[str, Any]:
        return {
            "font_size": self.font_size,
            "dark_mode": self.dark_mode,
            **super().get_config()
        }

    def __del__(self) -> None:
        if hasattr(self, 'log_file'):
            self.log_file.close()
        if not self.user_log_path and os.path.exists(self.log_path):
            os.remove(self.log_path)