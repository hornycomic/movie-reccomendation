import openai
import gradio

openai.api_key = "sk-BTHfwU2AztUfTqMV9hqsDtfryIWtBZuAWvoyL4IjtST3BlbkFJHHeSUrR8jTgWxrAbNPCDulRtD225_N91TvWj1-LMUA"

messages = [{"role": "system", "content": "You are a Movie reccomendation chat bot working for Ayan Pathak"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Ayan's Reccomendation Engine")

demo.launch(share=True)