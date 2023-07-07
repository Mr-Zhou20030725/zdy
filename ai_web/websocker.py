# websocket_server.py
import asyncio
import websockets
from multiprocessing import Process, Queue, set_start_method


class WebSocketServer:
    def __init__(self):
        self.clients = set()
        self.queue = Queue()
        self.sendqueue = Queue()
        self.can_send = False
        self.message = None

    async def receive(self, websocket, path):
        # 添加新的客户端到集合中
        self.clients.add(websocket)
        print('有新的客户端连接')
        FRIST = True
        SystemLocked = False
        try:
            async for message in websocket:
                print(f'接收到客户端发来的消息：{message}')
                self.queue.put(message)
                print("Message added to queue.")
                print("Queue size: ", self.queue.empty())
                # 检查API 调用API之后获得返回
                # txtresult = check_API(message)
                # if txtresult != "" and txtresult != None and txtresult != " ":
                #     SystemLocked = True

                # 判断指令结束
                if FRIST:
                    result = self.wake_up_3()
                    FRIST = False
                    result = result.strip()
                else:
                    result = self.sendqueue.get()

                result = result.strip()
                await websocket.send(result)

        except websockets.exceptions.ConnectionClosed:
            print('客户端断开连接')

        finally:
            # 移除已断开连接的客户端
            self.clients.remove(websocket)

    def wake_up_3(self):
        # here you put your wake_up_3 implementation
        return "你好，我是小冰，有什么可以帮助你"

    async def send(self, message):
        # 向所有已连接的客户端发送消息
        for client in self.clients:
            if client.open:
                await client.send(message)

    async def start_server(self):
        async with websockets.serve(self.receive, "localhost", 8888):
            print("WebSocket 服务器已启动")
            await asyncio.Future()  # 阻止停止

    def run(self):
        self.process = Process(target=self._run_process)
        self.process.start()

    def _run_process(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.start_server())
        loop.run_forever()

    def stop(self):
        self.process.terminate()
        self.process.join()

    def send_message(self, message):
        self.sendqueue.put(message)

    def receive_message(self):
        # This method will block until a message is available.
        # print("Waiting for message...")
        # import time
        # while self.queue.empty():
        #     print("Queue is empty, waiting...")
        #     time.sleep(1)
        return self.queue.get()
