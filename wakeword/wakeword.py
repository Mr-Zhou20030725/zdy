import struct
import pvporcupine
import pyaudio
import subprocess
PICOVOICE_API_KEY = "cfOm5AnThZ9Ajlt2xn3LsH87kmzqWhMWY/LtLTNZOswPpVAuyDXsmQ=="
keyword_path = "d:\\VMware share\\debot\\src\\嗨小疆_zh_Windows_v2_2_0.ppn"
pv = "d:\\VMware share\\debot\\src\\porcupine_params_zh.pv"
#启动ai_server.py
class PicoWakeWord:
    def __init__(self, PICOVOICE_API_KEY, keyword_path, model_path):
        self.PICOVOICE_API_KEY = PICOVOICE_API_KEY
        self.keyword_path = keyword_path
        self.model_path = model_path
        self.porcupine = pvporcupine.create(
            access_key=self.PICOVOICE_API_KEY,
            keyword_paths=[self.keyword_path],
            model_path=self.model_path
        )
        self.myaudio = pyaudio.PyAudio()
        self.stream = self.myaudio.open(
            input_device_index=0,
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    def detect_wake_word(self):
        audio_obj = self.stream.read(self.porcupine.frame_length, exception_on_overflow=False)
        audio_obj_unpacked = struct.unpack_from("h" * self.porcupine.frame_length, audio_obj)
        keyword_idx = self.porcupine.process(audio_obj_unpacked)
        return keyword_idx

class Wake_word:
    def __init__(self):
        self.picowakeword = PicoWakeWord(PICOVOICE_API_KEY, keyword_path, pv)
    #堵塞的唤醒词检测
    def wait(self):
        while True:
            print(".",end="")
            audio_obj = self.picowakeword.stream.read(self.picowakeword.porcupine.frame_length, exception_on_overflow=False)
            audio_obj_unpacked = struct.unpack_from("h" * self.picowakeword.porcupine.frame_length, audio_obj)
            keyword_idx = self.picowakeword.porcupine.process(audio_obj_unpacked)
            if keyword_idx >= 0:
                return True
   



if __name__ == '__main__':
    wake_word = Wake_word()
    wake_word.wait()
    