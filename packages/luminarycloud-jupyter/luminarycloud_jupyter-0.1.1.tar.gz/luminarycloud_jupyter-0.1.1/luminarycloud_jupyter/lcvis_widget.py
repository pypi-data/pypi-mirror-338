import anywidget
import array
import pathlib
import traitlets
from typing import Any, Optional

base_path = pathlib.Path(__file__).parent / "static"


class LCVisWidget(anywidget.AnyWidget):
    _esm: pathlib.Path = base_path / "lcvis.js"

    # TODO: we'll bundle the single threaded wasm here for vanilla Jupyter

    data: traitlets.Bytes = traitlets.Bytes().tag(sync=True)
    last_screenshot: Optional[bytes] = None

    camera_position: traitlets.List = traitlets.List().tag(sync=True)
    camera_look_at: traitlets.List = traitlets.List().tag(sync=True)
    camera_up: traitlets.List = traitlets.List().tag(sync=True)

    # TODO will: we should also expose pan as a param on the camera

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.on_msg(self.receive_widget_message)

    def receive_widget_message(self, widget: Any, content: str, buffers: list[bytes]) -> None:
        if content == "screenshot taken":
            self.last_screenshot = buffers[0]

    def take_screenshot(self) -> None:
        self.last_screenshot = None
        self.send({"cmd": "screenshot"})

    def set_surface_visibility(self, surface_id: str, visible: bool) -> None:
        print(f"Setting visibility for {surface_id} to {visible}")
        self.send(
            {
                # TODO: put these in some shared JSON defs/constants file for cmds?
                "cmd": "set_surface_visibility",
                "surface_id": surface_id,
                "visible": visible,
            }
        )

    def set_surface_color(self, surface_id: str, color: list[float]) -> None:
        if len(color) != 3:
            raise ValueError("Surface color must be list of 3 RGB floats, in [0, 1]")
        if any(c < 0 or c > 1 for c in color):
            raise ValueError("Surface color must be list of 3 RGB floats, in [0, 1]")
        self.send(
            {
                # TODO: put these in some shared JSON defs/constants file for cmds
                "cmd": "set_surface_color",
                "surface_id": surface_id,
            },
            [array.array("f", color)],
        )

    def reset_camera(self) -> None:
        self.send({"cmd": "reset_camera"})
