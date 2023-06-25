from http.server import BaseHTTPRequestHandler, HTTPServer
import json

host = "127.0.0.1"
port = 9999

# data = {"id": 1, "title": "study", "description": "study html and css"}

todo_lst = []


class ToDo(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        content = json.dumps(todo_lst)
        self.wfile.write(bytes(content, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        post_data_dict = json.loads(post_data.decode("utf-8"))
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        # content = json.dumps(data).encode("utf-8")
        todo_lst.append(post_data_dict)
        self.wfile.write(post_data)


server = HTTPServer((host, port), ToDo)
print("Server running")

server.serve_forever()
server.server_close()
print("Server stopped")
