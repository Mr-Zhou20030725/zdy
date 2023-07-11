# version: Python3
import struct
import pvporcupine
import pyaudio
import os
from DobotEDU import *
import zdy.tts as tts  #导入tts模块
import zdy.ai_use as ai_use #导入ai_use模块
import zdy.speechModule.speech2test as speech2test #导入语音识别模块
import zdy.wakeword.wakeword as Wakeword    #导入wakeword模块
import zdy.task.led as led  #导入led模块
import subprocess
import zdy.api
def main():
    wakeword = Wakeword.Wake_word() #唤醒词检测
    listen = speech2test.BaiduASR() #语音识别
    api = zdy.api.API() #api 
    #启动大模型
    subprocess.Popen("python  d:\\越疆\DobotLab\\resources\\dobotlink\\resources\\dobotlink-win\\tool\py38\\Lib\\zdy\\ai_web\\ai_web_start.py",shell=True)
    
    while True:
        if wakeword.wait(): #唤醒词检测
            led.set_breath_led()
            print("唤醒成功")
            word = listen.speech_to_text()
            if word == "" or len(word) <= 1:
                continue
            ai_use.sendMsg("嗨小疆"+word)
            msg = ai_use.getMsg()
            if api.is_api_call(msg):#判断是否是api调用
                res = api.do_api(msg)
                if res['is_success']:
                    ai_use.sendMsg(res['result'])
                else:
                    ai_use.sendMsg('失败')
                msg = ai_use.getMsg()
            tts.voice(msg)
            #开启多轮对话
            while not ai_use.isEnd(msg):
                word = listen.speech_to_text()
                if word == "" or len(word) <= 1:
                    break
                ai_use.sendMsg(word)
                msg = ai_use.getMsg()
                if api.is_api_call(msg):#判断是否是api调用
                    res = api.do_api(msg)
                    if res['is_success']:
                        ai_use.sendMsg(res['result'])
                    else:
                        ai_use.sendMsg('失败')
                    msg = ai_use.getMsg()
                tts.voice(msg)
            print("对话结束")
            led.set_blue_led()
                    
if __name__ == '__main__':
    main()