from http.server import BaseHTTPRequestHandler
import json
import openai

# Hardcoded API key (not recommended for production)
openai.api_key = "sk-NiThu1fh3xP07MZ6aBHOLJleYIhtWFxblHI-tpAmCzT3BlbkFJPaaE4Biuz2aZufM7Me9HnP8YhquAFK2eP6m8KYJNgA"

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
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("This endpoint accepts POST requests only. Please send a POST request with a JSON body containing a 'user_input' field.".encode('utf-8'))

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            user_input = data.get('user_input', '')
            if not user_input:
                raise ValueError("'user_input' field is required in the request body")
            
            response = CustomChatGPT(user_input)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"response": response}).encode('utf-8'))
        except Exception as e:
            self.send_error(400, str(e))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type")
        self.end_headers()