from http.server import BaseHTTPRequestHandler
import json
import openai

openai.api_key = "sk-NiThu1fh3xP07MZ6aBHOLJleYIhtWFxblHI-tpAmCzT3BlbkFJPaaE4Biuz2aZufM7Me9HnP8YhquAFK2eP6m8KYJNgA"  # Replace with your actual API key

messages = [{"role": "system", "content": "You are a Movie recommendation chat bot working for Ayan Pathak"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        user_input = data.get('user_input', '')
        response = CustomChatGPT(user_input)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"response": response}).encode('utf-8'))
        return