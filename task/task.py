from DobotEDU import *
import zdy.task.led as led
from zdy.tts import voice
def get_power():#电源
    led.white_led()
    pwv=go.get_power_voltage()
    return pwv
def pgotop():#点到点
    led.white_led()
    go.set_ptp_with_l( x=250, y=0, z=0, r=0, mode=0)
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
def clean():
    m_lite.set_homecmd()
    m_lite.set_endeffector_gripper(enable=True, on=False)
    m_lite.set_ptpcmd(ptp_mode=0, x=270, y=0, z=-70, r=0)
    m_lite.set_endeffector_gripper(enable=True, on=True)
    m_lite.set_ptpcmd(ptp_mode=0, x=260, y=0, z=125, r=0)
def playcat():
    led.white_led()
    beta_go.grab_obj( 1)
    voice("喵 喵喵")
    ###
# def ssss



