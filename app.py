import gradio as gr
gr.close_all()

def getDetails(name, age, preference, hobbies):
  return f" "

demo = gr.Interface(
    fn=getDetails,
    inputs = [gr.Textbox(label="Name: "),
        gr.Slider(label="Age: "),
        gr.Radio(label="Subject Preference: ", choices=['C','C#','Python']),
        gr.Checkboxgroup(label='Hobbies:', choices=['Painting','Singing','Dancing'])
    ],
    outputs=[gr.Textbox()]
)
demo.launch()

