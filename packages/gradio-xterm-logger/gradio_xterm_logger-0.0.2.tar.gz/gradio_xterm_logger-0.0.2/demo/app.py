import gradio as gr
from gradio_xterm_logger import GradioXtermLogger


with gr.Blocks() as demo:
    terminal_a = GradioXtermLogger(
        label="Terminal Output (Custom Log File)",
        log_path="inference_log.log",
        font_size=12,
        dark_mode=True,
        every=0.5
    )

    terminal_b = GradioXtermLogger(
        label="Terminal Output (Current Terminal)",
        show_current_terminal=True,
        font_size=12,
        dark_mode=False,
        every=0.5
    )

if __name__ == "__main__":
    demo.launch()