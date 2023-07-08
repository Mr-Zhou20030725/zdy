# version: Python3
from DobotEDU import *
class base:
    def ctf(self,text):#车到地
        object_class=text
        beta_go.grab_obj_cartofloor(object_class)
    def ftc(self,text):#地到车
        object_class=text
        beta_go.grab_obj_cartofloor(object_class)
    def xy(self,x, y, Vx, Vy,mode):#xy平移
        go.set_running_mode(mode)
        go.set_move_dist(x, y, Vx, Vy)
    def round(self, v, r, angle,mode):#半径圆弧
        go.set_running_mode(mode)
        go.set_arc_rad( velocity=v, radius=r, angle=angle, mode=1)
    def rotate(self,r,vr.mode):#旋转
        go.set_running_mode(mode)
        go.set_rotate(r,vr)
    def set_Buzzer(self,mode):#蜂鸣器
        go.set_buzzer_sound(index=mode, tone=50, beat=2)



