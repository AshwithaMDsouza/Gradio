
import gradio as gr
gr.close_all()

def getDetails(name, age, preference, hobbies):
    return f"Name: {name}\nAge: {age}\nSubject Preference: {preference}\nHobbies: {', '.join(hobbies)}"

demo = gr.Interface(
    fn=getDetails,
    inputs=[
        gr.Textbox(label="Name: "),
        gr.Slider(minimum=1, maximum=100, label="Age: "),
        gr.Radio(label="Subject Preference: ", choices=['C', 'C#', 'Python']),
        gr.CheckboxGroup(label="Hobbies: ", choices=['Painting', 'Singing', 'Dancing'])
    ],
    outputs=gr.Textbox()
)
demo.launch()


