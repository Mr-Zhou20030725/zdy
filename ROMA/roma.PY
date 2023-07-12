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
    #启动大模型
    subprocess.Popen("python  d:\\越疆\DobotLab\\resources\\dobotlink\\resources\\dobotlink-win\\tool\py38\\Lib\\zdy\\ai_web\\ai_web_start.py",shell=True)
    
    while True:
        if wakeword.wait(): #唤醒词检测
            led.set_breath_led()
            print("唤醒成功")
            time.sleep(4)
            led.set_green_led()
            tts.voice("收到，主人，执行宠物跟踪任务")
            led.set_yellow_led()
            #转圈
            go.set_rotate(180,10)
            tts.voice("宠物找到了")
            led.set_blue_led()
                    
if __name__ == '__main__':
    main()