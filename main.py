import cv2 , time 
from cvzone.HandTrackingModule import HandDetector
from Modules.directkeys import PressKey , ReleaseKey , space_pressed
# webcam!
video = cv2.VideoCapture(0)
# 0 for first webcam connect 

# dectect hand
dector = HandDetector(detectionCon=0.8 , maxHands=1)

# vari
space_key_pressed = space_pressed
# ////
time.sleep(2.0)
                                                                                             
current_key_pressed = set()



  
# logics of camera
while True:   
    
    _,frame=video.read()
    KeyPressed = False
    SpacePressed = False
    key_count=0
    key_pressed=0
    hands,img=dector.findHands(frame)
    if hands:
        lmmlist = hands[0]
        fingup = dector.fingersUp(lmmlist)
        if fingup==[0,0,0,0,0]:
            cv2.putText(frame,"Finger Count : 0", (59,108),cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,255,255),1 ,cv2.LINE_AA)
            cv2.putText(frame,"Jumping : True", (423,104),cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,255,255),1 ,cv2.LINE_AA)
        #    Click The Space Keyy
            PressKey(space_key_pressed)
            current_key_pressed.add(space_key_pressed)
            key_pressed=space_key_pressed
            KeyPressed = True
            key_count = key_count+1
        if fingup==[0,1,0,0,0]:
            cv2.putText(frame,"Jumping : False", (423,104),cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,255,255),1 ,cv2.LINE_AA)
            cv2.putText(frame,"Finger Count : 1", (59,108),cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,255,255),1 ,cv2.LINE_AA)
        if fingup==[0,1,1,0,0]:
            cv2.putText(frame,"Jumping : False", (423,104),cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,255,255),1 ,cv2.LINE_AA)
            cv2.putText(frame,"Finger Count : 2", (59,108),cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,255,255),1 ,cv2.LINE_AA)
        if fingup==[0,1,1,1,0]:
            cv2.putText(frame,"Finger Count : 3", (59,108),cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,255,255),1 ,cv2.LINE_AA)
            cv2.putText(frame,"Jumping : False", (423,104),cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,255,255),1 ,cv2.LINE_AA)
        if fingup==[0,1,1,1,1]:
            cv2.putText(frame,"Finger Count : 4", (59,108),cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,255,255),1 ,cv2.LINE_AA)
            cv2.putText(frame,"Jumping : False", (423,104),cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,255,255),1 ,cv2.LINE_AA)
        if fingup==[1,1,1,1,1]:
            cv2.putText(frame,"Finger Count : 5", (59,108),cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,255,255),1 ,cv2.LINE_AA)
            cv2.putText(frame,"Jumping : False", (423,104),cv2.FONT_HERSHEY_COMPLEX ,1 ,(255,255,255),1 ,cv2.LINE_AA)
        if not KeyPressed and len(current_key_pressed) != 0:
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()
        elif key_count==1 and len(current_key_pressed)==2:
            for key in current_key_pressed:
                if key_pressed!=key:
                    ReleaseKey(key)
            current_key_pressed = set()
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()       

    
    cv2.imshow('Frame',frame)
    k = cv2.waitKey(1)
    if k==ord('q'):
        break


# realse 

video.release()    
cv2.destroyAllWindows()