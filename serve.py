import socket
import cv2
import numpy
from multiprocessing import Process, Queue

class ImageReceiver:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(True)
        self.conn, self.addr =None, None
        print('等待客户端连接...,port:', port)
        self.queue = Queue()
    @staticmethod
    def recv_size(sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf:
                return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def receive_images(self):
        self.conn, self.addr = self.sock.accept()
        while True:
            length = self.recv_size(self.conn, 16).decode()
            if isinstance(length, str):
                stringData = self.recv_size(self.conn, int(length))
                data = numpy.fromstring(stringData, dtype='uint8')
                decimg = cv2.imdecode(data, 1)
                cv2.imshow('Camera 1', decimg)
                cv2.waitKey(1)

def main(port):
    
    print('开启接收进程, port:', port)
    receiver1 = ImageReceiver('', port)
    print('开启接收进程1')
    receiver1.receive_images()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    import sys
    port = int(sys.argv[1])
    main(port)
