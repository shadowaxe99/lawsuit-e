
from http.server import BaseHTTPRequestHandler
import json
import openai

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        api_key = data['api_key']
        prompt = data['prompt']
        model = data.get('model', 'gpt-3.5-turbo')

        openai.api_key = api_key

        try:
            response = openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=1024
            )
            document = response.choices[0].text
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"document": document}).encode())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

        return
