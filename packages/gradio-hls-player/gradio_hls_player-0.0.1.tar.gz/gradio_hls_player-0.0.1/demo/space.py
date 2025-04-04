
import gradio as gr
from app import demo as app
import os

_docs = {'GradioHLSPlayer': {'description': 'A base class for defining methods that all input/output components should have.', 'members': {'__init__': {'value': {'type': 'typing.Dict[str, typing.Any][str, typing.Any]', 'default': 'None', 'description': None}}, 'postprocess': {'value': {'type': 'typing.Dict[str, typing.Any][str, typing.Any]', 'description': "The output data received by the component from the user's function in the backend."}}, 'preprocess': {'return': {'type': 'typing.Dict[str, typing.Any][str, typing.Any]', 'description': "The preprocessed input data sent to the user's function in the backend."}, 'value': None}}, 'events': {'play': {'type': None, 'default': None, 'description': ''}, 'pause': {'type': None, 'default': None, 'description': ''}, 'error': {'type': None, 'default': None, 'description': ''}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'GradioHLSPlayer': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_hls_player`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  
</div>

Python library for easily interacting with trained machine learning models
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_hls_player
```

## Usage

```python
import gradio as gr
from gradio_hls_player import GradioHLSPlayer

def create_hls_app():
    with gr.Blocks() as demo:
        gr.Markdown("# Gradio HLS Stream Player")
        
        with gr.Row():
            url_input = gr.Textbox(
                label="Enter M3U8 URL",
                value="https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8",
                placeholder="Paste HLS stream URL here..."
            )
            submit_btn = gr.Button("Load Stream", variant="primary")
        
        with gr.Row():
            width_slider = gr.Slider(
                label="Width", 
                minimum=320, 
                maximum=1920, 
                value=640, 
                step=10
            )
            height_slider = gr.Slider(
                label="Height", 
                minimum=180, 
                maximum=1080, 
                value=360, 
                step=10
            )
        
        autoplay_checkbox = gr.Checkbox(label="Autoplay", value=False)
        hide_controls_checkbox = gr.Checkbox(label="Hide Controls", value=False)
        
        hls_player = GradioHLSPlayer(
            value={
                "url": "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8",
                "width": 640,
                "height": 360,
                "autoplay": False,
                "hide_player_control_bar": False
            },
            label="HLS Video Player"
        )
        
        def update_player(url, width, height, autoplay, hide_controls):
            return {
                "url": url,
                "width": width,
                "height": height,
                "autoplay": autoplay,
                "hide_player_control_bar": hide_controls
            }

        url_input.change(
            fn=update_player,
            inputs=[url_input, width_slider, height_slider, autoplay_checkbox, hide_controls_checkbox],
            outputs=hls_player
        )
        submit_btn.click(
            fn=update_player,
            inputs=[url_input, width_slider, height_slider, autoplay_checkbox, hide_controls_checkbox],
            outputs=hls_player
        )
    
    return demo

if __name__ == "__main__":
    app = create_hls_app()
    app.launch()
```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `GradioHLSPlayer`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["GradioHLSPlayer"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["GradioHLSPlayer"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, the preprocessed input data sent to the user's function in the backend.
- **As output:** Should return, the output data received by the component from the user's function in the backend.

 ```python
def predict(
    value: typing.Dict[str, typing.Any][str, typing.Any]
) -> typing.Dict[str, typing.Any][str, typing.Any]:
    return value
```
""", elem_classes=["md-custom", "GradioHLSPlayer-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          GradioHLSPlayer: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
