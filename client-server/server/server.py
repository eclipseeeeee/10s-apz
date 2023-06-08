from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MessageService:
    messages = []

    @classmethod
    def get_messages(cls):
        return cls.messages

    @classmethod
    def add_message(cls, message):
        cls.messages.append(message)


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(MessageService.get_messages()).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        message = json.loads(post_data)['message']
        MessageService.add_message(message)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Message added')


def run_server():
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running...')
    httpd.serve_forever()
