from DobotEDU import *
import led
class task:
    def get_power():#电源
        led.white_led()
        pwv=go.get_power_voltage(self)
        return pwv
    def pgotop():#点到点
        led.white_led()
        go.set_ptp_with_l(self, x=250, y=0, z=0, r=0, mode=0)
    def findpet():
        go.set_running_mode(1)
        led.white_led()
        voice("开始寻找宠物")
        go.set_move_dist(45, 45, 2, 2)
        voice("未检测到宠物")
        go.set_move_dist(-45, 45, 2, 2)
        voice("未检测到宠物")
        go.set_move_dist(-45, -45, 2, 2)
        voice("未检测到宠物")
        go.set_move_dist(45, -45, 2, 2)
    def playcat():
        led.white_led()
        beta_go.grab_obj(self, 1)
        voice("喵 喵喵")
        ###
    def 



