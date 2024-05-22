import subprocess
import gradio as gr
new_line = '\n'


def predict(input1):
    result = subprocess.run(['python', 'z2ai_text_2_image_predict_client.py',
                             input1], capture_output=True, text=True)
    result = result.stdout.replace(new_line, ',')
    result = result[:-1]
    return result


title = "Z2AI z2ai_text_2_image Service"
inputs = [gr.Textbox(label='Input')]
outputs = [gr.Image(type="filepath", label='Output')]

interface = gr.Interface(predict, inputs=inputs, outputs=outputs,
                         title=title)
interface.launch()
