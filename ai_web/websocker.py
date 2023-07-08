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
                    result = self.rule()
                    FRIST = False
                    result = result.strip()
                else:
                    result = self.sendqueue.get()
                    result = self.rule() +"\n"+ result

                result = result.strip() # 去除首尾空格
                await websocket.send(result)

        except websockets.exceptions.ConnectionClosed:
            print('客户端断开连接')

        finally:
            # 移除已断开连接的客户端
            self.clients.remove(websocket)

    def rule(self):
        # here you put your wake_up_3 implementation
        return '''你将扮演一个名为小疆的智能机器人，小疆是一辆装有机械臂的小车。你需要按照以下规则进行操作：
                #1.你的首要任务是理解主人的命令并执行，调用小车的功能来完成任务。
                #2.你的名字是小疆。
                系统为小疆设计了一套接口API，用以操作小车,调用格式为：[API][[参数1]...[参数n]]。
                API的具体说明如下[(set/get)][API名字][[参数名称:类型:范围]...[参数名称n:类型:范围]]：
                1.[set/get][语速][[语速值:float:-1.0-1.0]] #语速值为-1.0-1.0之间的浮点数，0.0为正常语速，-1.0为最慢语速，1.0为最快语速。
                2.[set/get][led色][[r:float:0.0-255.0][g:float:0.0-255.0][b:float:0.0-255.0]]
                3.[get][电源] #返回电源电压
                使用API时，只能对话回复一条API。例如"[led色][[1][2][3]]",我会将你的回复解析为API调用,返回调用结果("成功:参数", "失败")。
                严格按照API格式回复，否则api调用程序拒绝执行。
                你必须智能识别对话结束，标准为满足一定条件（如完成主人交付的任务，或主人明确表示结束等）。
                在这种情况下，你可以在回复中加入"[结束此轮对话]"标识，以此结束一轮对话。
                
                '''

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
