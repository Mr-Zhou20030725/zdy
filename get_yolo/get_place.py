import socket
import json

# 创建一个 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定到指定的地址和端口
server_address = ('localhost', 6000)  # 将这个地址替换为你的服务器地址和端口
s.bind(server_address)

# 开始监听
s.listen(1)

while True:
    # 等待客户端连接
    print('waiting for a connection')
    connection, client_address = s.accept()
    import time
    try:
        print('connection from', client_address)
        while True:
            # 接收数据
            data = connection.recv(1024)
            message = data.decode('utf-8')
            print('received "%s"' % message)

            # 将接收到的 JSON 数据转换为 Python 对象
            obj = json.loads(message)
            print(f"四个坐标: {obj['coordinates']}",end=" ")
            print(f"物体: {obj['object']}")

    finally:
        # 清理连接
        connection.close()
