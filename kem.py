#Object Tracking
import time
import numpy as np
import cv2
 
second = 0
 
width, height = 160, 120
camera = cv2.VideoCapture(0)
camera.set(3,width) 
camera.set(4,height) 
 
l_motor = 18
left_front   =  22
left_back   =  27
 
r_motor = 23
right_front   = 25
right_back  =  24
 
 
def Motor_Init():
 pass
 
def Direction_Init():
    pass
 
 
def Servo_Init():
    pass
 
def Init():
    pass
 
 
def Front(speed):
    print("前进")
    
def Back(speed):
    print("后退")
 
def Left(speed):
    print("左转")
 
def Right(speed):
    print("右转")
 
 
def Stop():
    print("停止")
 
def set_servo_angle(channel,angle): #设置舵机角度
    angle=4096*((angle*11)+500)/20000 #转换角度
    print(angle)
 
 
def Image_Processing():
    # Capture the frames
    ret, frame = camera.read()
    # Crop the image
    image = frame
    cv2.imshow('frame',frame)
    # to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    # Gausi blur
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #brighten
    blur = cv2.convertScaleAbs(blur, None, 1.5, 30)
    #to binary
    ret,binary = cv2.threshold(blur,150,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('binary',binary)
    #Close
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17,17))
    close = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('close',close)
    #get contours
    binary_c,contours,hierarchy = cv2.findContours(close, 1, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image, contours, -1, (255,0,255), 2)
    cv2.imshow('image', image)
    return frame, contours
 
 
def Get_Coord(img, contours):
    image = img.copy()
    try:
        contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(image, contour, -1, (255,0,255), 2)
        cv2.imshow('new_frame', image)
        # get coord
        M = cv2.moments(contour)
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
        print(x, y) 
        return x,y
        
    except:
        print ('no objects')
        return 0,0
    
    
def Move(x,y):
    global second
    #stop
    if x==0 and y==0:
        Stop()
    #go ahead
    elif width/4 <x and x<(width-width/4):
        Front(70)
    #left
    elif x < width/4:
        Left(50)
    #Right
    elif x > (width-width/4):
        Right(50)
    
    
if __name__ == '__main__':
    Init()
    
    set_servo_angle(4, 110)     #top servo     lengthwise
    #0:back    180:front    
    set_servo_angle(5, 90)     #bottom servo  crosswise
    #0:left    180:right  
    
    while 1:
        # 1 Image Process
        img, contours = Image_Processing()
 
        # 2 get coordinates
        x, y = Get_Coord(img, contours)
 
        # 3 Move
        Move(x,y)
        
        # must include this codes(otherwise you can't open camera successfully)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            Stop()
            GPIO.cleanup()    
            break
    
    #Front(50)
    #Back(50)
    #$Left(50)
    #Right(50)
    #time.sleep(1)
    #Stop()
 