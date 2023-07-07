# version: Python3
import struct
import pvporcupine
import pyaudio
import os
from DobotEDU import *
import zdy.tts as tts  #导入tts模块
from ai_use import *     #导入ai_use模块
import zdy.speechModule.speech2test as speech2test #导入语音识别模块
import zdy.wakeword.wakeword as Wakeword    #导入wakeword模块
import zdy.task.led as led  #导入led模块
import subprocess
def main():
    wakeword = Wakeword.Wake_word() #唤醒词检测
    listen = speech2test.BaiduASR() #语音识别
    #启动web
    subprocess.Popen("python  d:\\越疆\DobotLab\\resources\\dobotlink\\resources\\dobotlink-win\\tool\py38\\Lib\\zdy\\ai_web_start.py",shell=True)
    
    while True:
        if wakeword.wait(): #唤醒词检测
            # led.breath_led()#呼吸灯
            print("我听到了！")
            tts.voice("我在,有什么可以帮助你的吗？")
            word = listen.speech_to_text()
            sendMsg(word)
            msg = getMsg()
            tts.voice(msg)
            # led.blue_led()
                    
                                
                
                
                
if __name__ == '__main__':
    main()