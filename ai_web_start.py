from http.server import BaseHTTPRequestHandler, HTTPServer
import tts as tts
from   ai_web.websocker import  WebSocketServer
HOST_NAME = 'localhost'
PORT_NUMBER = 8000


if __name__ == '__main__':
    server = WebSocketServer()
    server.run()
    message = server.receive_message()
    print(f"收到的消息是：{message}")
    message = server.receive_message()
    print(f"Received2: {message}")
    # tts.voice(message)
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(server.receive_message().encode())

        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            message = self.rfile.read(content_length).decode('utf-8')
            print(f"收到的消息是：{message}")
            server.send_message(message)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("已发送".encode('utf-8'))

    web_server = HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
    print(f"Server started on http://{HOST_NAME}:{PORT_NUMBER}/")
    web_server.serve_forever()
