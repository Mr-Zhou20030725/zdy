# encoding
import pygame
import subprocess
from aiohttp import TCPConnector
import edge_tts


VOICE = "zh-CN-XiaoyiNeural"
TEXT = ""
OUTPUT_FILE = ""

async def _main() -> None:
    global TEXT
    global OUTPUT_FILE
    with open(OUTPUT_FILE, "wb") as f:
        pass
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)


def play_audio_with_pygame(audio_file_path):
    # 代码来自Linky的贡献
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()


def __voice(text):
    try:
        import zdy.api
        api = zdy.api.API() #api

        res = api.do_api("[get][语速]")
        voice_speed = float(res['result'][3:])
        voice_speed = int(voice_speed*100)
    except:
        voice_speed = 10
    if voice_speed < 0:
        voice_speed = "="+str(voice_speed) + "%"
    else:
        voice_speed = " +"+str(voice_speed) + "%"
    print(voice_speed)
    global OUTPUT_FILE
    global TEXT
    TEXT = text
    OUTPUT_FILE = "1"+".mp3"
    #处理文本：
    TEXT = TEXT.replace(" ", ",")
    TEXT = TEXT.replace("\n", ".")
    
    print("语音开始")
    
    import os
    cmd = "edge-tts --voice "+VOICE+" --text \""+TEXT+"\" --write-media "+OUTPUT_FILE+" --proxy http://127.0.0.1:33210"+ " --rate"+str(voice_speed)
    cmd_noproxy = "edge-tts --voice "+VOICE+" --text \""+TEXT+"\" --write-media "+OUTPUT_FILE
    os.system(cmd)
    try:
        import zdy.audio.audio_sender as audio_sender
        audio_sender.send_audio(OUTPUT_FILE)
        from playsound import playsound
        playsound(OUTPUT_FILE)
    except:
        play_audio_with_pygame(OUTPUT_FILE)
    # del
    import os
    # os.remove(OUTPUT_FILE)

    # except:
    print("语音完成")

def voice(TEXT):
    import threading
    t = threading.Thread(target=__voice, args=(TEXT,))
    t.start()
    t.join()

if __name__ == "__main__":
    voice(
        '''
        你好
        '''
    )