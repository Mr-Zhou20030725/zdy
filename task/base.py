# version: Python3
from DobotEDU import *
class base:
    def ctf(self,text):#车到地,self为beta_go
        object_class=text
        beta_go.grab_obj_cartofloor(object_class)
    def ftc(self,text):#地到车,self为beta_go
        object_class=text
        beta_go.grab_obj_cartofloor(object_class)
    def xy(self,x, y, Vx, Vy,mode):#xy平移
        go.set_running_mode(mode)
        go.set_move_dist(x, y, Vx, Vy)
    def rotate(self,r,vr,mode):#旋转
        go.set_running_mode(mode)
        go.set_rotate(r,vr)
    def set_Buzzer(self,mode):#蜂鸣器
        go.set_buzzer_sound(index=mode, tone=50, beat=2)



