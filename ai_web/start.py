# main.py
from ai_web.websocker import WebSocketServer
import tts
# 1.receive_message：堵塞 直到收到消息
# 2.send_message：发送消息

if __name__ == "__main__":
    server = WebSocketServer()
    server.run()
    message = server.receive_message()
    print(f"收到的消息是：{message}")
    message = server.receive_message()
    print(f"Received2: {message}")
    tts.voice(message)
    server.send_message("Hello from main.py")
