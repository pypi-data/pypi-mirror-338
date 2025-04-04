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