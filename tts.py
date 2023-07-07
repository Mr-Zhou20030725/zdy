# encoding
import pygame
import subprocess
import asyncio
from aiohttp import TCPConnector
import edge_tts
import random
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


def voice(text):
    # try:
    global OUTPUT_FILE
    global TEXT
    TEXT = text
    OUTPUT_FILE = "1"+".mp3"
    # asyncio.run(_main())
    # import os
    cmd = "edge-tts --voice "+VOICE+" --text \""+TEXT+"\" --write-media "+OUTPUT_FILE
    subprocess.call(cmd, shell=True)
    try:
        from playsound import playsound
        playsound(OUTPUT_FILE)
    except:
        play_audio_with_pygame(OUTPUT_FILE)
    # del
    import os
    os.remove(OUTPUT_FILE)

    # except:
    print("语音完成")


if __name__ == "__main__":
    voice("你好")
