import socket
import os

def send_audio(file_path):
    # 判断文件是否存在
    if not os.path.exists(file_path):
        print('File not exists.')
        return

    # 建立socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定IP和端口
    s.bind(('0.0.0.0', 8000))

    # 监听，等待连接 1 表示最大连接数
    s.listen(1)
    print('Waiting for connection...')

    while True:
        # 建立连接
        conn, addr = s.accept()
        print('Connected by', addr)

        # 打开文件，读取文件内容，发送
        with open(file_path, 'rb') as f:
            l = f.read(1024)
            while l:
                conn.send(l)
                l = f.read(1024)
        break

    # 关闭连接
    conn.close()
    s.close()

if __name__ == '__main__':
    while 1:
        send_audio('1.mp3')
