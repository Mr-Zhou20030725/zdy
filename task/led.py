from DobotEDU import *
def set_breath_led():#呼吸灯
    go.set_rgb_light(number="LED_1", effect=4, r=100 ,g=0, b=0, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_2", effect=4, r=100 ,g=0, b=0, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_3", effect=4, r=100 ,g=0, b=0, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_4", effect=4, r=100 ,g=0, b=0, cycle=0.5, counts=1) 
def set_blue_led():
    go.set_rgb_light(number="LED_1", effect=0, r=0,g=0, b=255, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_2", effect=0, r=0,g=0, b=255, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_3", effect=0, r=0,g=0, b=255, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_4", effect=0, r=0,g=0, b=255, cycle=0.5, counts=1)
def set_red_led():
    go.set_rgb_light(number="LED_1", effect=0, r=255,g=0, b=0, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_2", effect=0, r=255,g=0, b=0, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_3", effect=0, r=255,g=0, b=0, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_4", effect=0, r=255,g=0, b=0, cycle=0.5, counts=1)
def set_green_led():
    go.set_rgb_light(number="LED_1", effect=0, r=0,g=255, b=0, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_2", effect=0, r=0,g=255, b=0, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_3", effect=0, r=0,g=255, b=0, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_4", effect=0, r=0,g=255, b=0, cycle=0.5, counts=1)
def set_yellow_led():
    go.set_rgb_light(number="LED_1", effect=0, r=255,g=255, b=0, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_2", effect=0, r=255,g=255, b=0, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_3", effect=0, r=255,g=255, b=0, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_4", effect=0, r=255,g=255, b=0, cycle=0.5, counts=1)
def set_purple_led():
    go.set_rgb_light(number="LED_1", effect=0, r=255,g=0, b=255, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_2", effect=0, r=255,g=0, b=255, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_3", effect=0, r=255,g=0, b=255, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_4", effect=0, r=255,g=0, b=255, cycle=0.5, counts=1)
def set_cyan_led():
    go.set_rgb_light(number="LED_1", effect=0, r=0,g=255, b=255, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_2", effect=0, r=0,g=255, b=255, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_3", effect=0, r=0,g=255, b=255, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_4", effect=0, r=0,g=255, b=255, cycle=0.5, counts=1)
def set_white_led():
    go.set_rgb_light(number="LED_1", effect=0, r=255,g=255, b=255, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_2", effect=0, r=255,g=255, b=255, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_3", effect=0, r=255,g=255, b=255, cycle=0.5, counts=1) 
    go.set_rgb_light(number="LED_4", effect=0, r=255,g=255, b=255, cycle=0.5, counts=1)

