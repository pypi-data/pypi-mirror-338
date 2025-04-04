from gradio.components.base import Component
from typing import Dict, Any

class GradioHLSPlayer(Component):
    EVENTS = ["play", "pause", "error"]
    
    def __init__(
        self, 
        value: Dict[str, Any] = None,
        **kwargs
    ):
        default_value = {
            "url": "",
            "width": 640,
            "height": 360,
            "autoplay": False,
            "hide_player_control_bar": False
        }
        super().__init__(value=value or default_value, **kwargs)
        self._component_name = "hlsplayer"

    @property
    def component_type(self):
        return "hlsplayer"

    def preprocess(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return payload

    def postprocess(self, value: Dict[str, Any]) -> Dict[str, Any]:
        return value

    def example_payload(self) -> Dict[str, Any]:
        return {
            "url": "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8",
            "width": 640,
            "height": 360,
            "autoplay": False,
            "hide_player_control_bar": False
        }

    def example_value(self) -> Dict[str, Any]:
        return self.example_payload()

    def api_info(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "HLS stream URL (.m3u8)"},
                "width": {"type": "number", "description": "Player width"},
                "height": {"type": "number", "description": "Player height"},
                "autoplay": {"type": "boolean", "description": "Autoplay video"},
                "hide_player_control_bar": {"type": "boolean", "description": "Hide controls"}
            },
            "required": ["url"]
        }