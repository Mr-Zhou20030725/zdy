import http.client

HOST_NAME = 'localhost'
PORT_NUMBER = 8000

# 发送GET请求
def __send_get_request():
    conn = http.client.HTTPConnection(HOST_NAME, PORT_NUMBER)
    conn.request('GET', '/')
    response = conn.getresponse()
    print('Response status:', response.status)
    reMsg = response.read().decode('utf-8')
    print('Response:'+reMsg)
    conn.close()
    return reMsg


# 发送POST请求
def __send_post_request(message):
    headers = {'Content-type': 'text/plain'}
    conn = http.client.HTTPConnection(HOST_NAME, PORT_NUMBER)
    conn.request('POST', '/', message.encode('utf-8'), headers)
    response = conn.getresponse()
    print('Response status:', response.status)
    print('Response body:', response.read().decode('utf-8'))
    conn.close()

def sendMsg(Msg):
    __send_post_request("(不要忘记识别智能对话是否结束和加上[结束此轮对话]哦)\n"+Msg)
    
def getMsg():
    return __send_get_request()
def isEnd(response):
    return "[结束此轮对话]" in response
if __name__=="__main__":
    sendMsg("你好")
    print('msg'+getMsg())