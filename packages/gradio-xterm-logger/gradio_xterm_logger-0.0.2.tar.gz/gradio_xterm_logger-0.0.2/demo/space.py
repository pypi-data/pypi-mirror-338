
import gradio as gr
from app import demo as app
import os

_docs = {'GradioXtermLogger': {'description': 'A base class for defining methods that all input/output components should have.', 'members': {'__init__': {'log_path': {'type': 'str | None', 'default': 'None', 'description': None}, 'dark_mode': {'type': 'bool', 'default': 'True', 'description': None}, 'font_size': {'type': 'int', 'default': '12', 'description': None}, 'show_current_terminal': {'type': 'bool', 'default': 'False', 'description': None}, 'n_lines': {'type': 'int', 'default': '40', 'description': None}, 'label': {'type': 'str | None', 'default': 'None', 'description': None}, 'info': {'type': 'str | None', 'default': 'None', 'description': None}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': None}, 'container': {'type': 'bool', 'default': 'True', 'description': None}, 'scale': {'type': 'int | None', 'default': 'None', 'description': None}, 'min_width': {'type': 'int | None', 'default': 'None', 'description': None}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': None}, 'visible': {'type': 'bool', 'default': 'True', 'description': None}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': None}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': None}, 'render': {'type': 'bool', 'default': 'True', 'description': None}, 'load_fn': {'type': 'typing.Optional[typing.Callable[..., typing.Any]][\n    typing.Callable[..., typing.Any][Ellipsis, Any], None\n]', 'default': 'None', 'description': None}, 'every': {'type': 'float | None', 'default': '0.5', 'description': None}}, 'postprocess': {'value': {'type': 'Any', 'description': "The output data received by the component from the user's function in the backend."}}, 'preprocess': {'return': {'type': 'Any', 'description': "The preprocessed input data sent to the user's function in the backend."}, 'value': None}}, 'events': {}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'GradioXtermLogger': []}}}

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
# `gradio_xterm_logger`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.2%20-%20orange">  
</div>

Python library for easily interacting with trained machine learning models
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_xterm_logger
```

## Usage

```python
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
```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `GradioXtermLogger`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["GradioXtermLogger"]["members"]["__init__"], linkify=[])




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
    value: Any
) -> Any:
    return value
```
""", elem_classes=["md-custom", "GradioXtermLogger-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          GradioXtermLogger: [], };
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
