import asyncio
from aiohttp import TCPConnector
import edge_tts
import random
VOICE = "zh-CN-XiaoyiNeural"
TEXT =""
OUTPUT_FILE = ""
import subprocess
# async def _main() -> None:
    
#     global TEXT
#     global OUTPUT_FILE
#     with open(OUTPUT_FILE, "wb") as f:
#         pass
#     communicate = edge_tts.Communicate(TEXT, VOICE)
#     await communicate.save(OUTPUT_FILE)


def voice(text):
    # try:
        global OUTPUT_FILE
        global TEXT
        TEXT = text
        OUTPUT_FILE = "1"+".mp3"
        # asyncio.run(_main())
        
        import os
        cmd="edge-tts --voice "+VOICE+" --text \""+TEXT+"\" --write-media "+OUTPUT_FILE
        
        subprocess.call(cmd, shell=True)
        
        from playsound import playsound
        playsound(OUTPUT_FILE)#
        #del
        # import os
        # os.remove(OUTPUT_FILE)

    # except:
        print("语音完成")
    
if __name__ ==   "__main__":
    voice("你好")


















