from ast import Continue
import cv2 as cv
import mediapipe as mp
from math import hypot

import time
from pynput.keyboard import Key, Controller


cap = cv.VideoCapture(0) 
 

mpHands = mp.solutions.hands 
hands = mpHands.Hands()   #complete the initialization configuration of hands   '''SHIV ANNA GROUP'''
mpDraw = mp.solutions.drawing_utils

keyboard = Controller()

while True:
    success,img = cap.read() 
    
    img=cv.flip(img,1) 
    # img = cv.resize(img, (1/2,1/2), interpolation=cv.INTER_CUBIC)

    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB) 
    
    lmList = [] 
    if results.multi_hand_landmarks: 
        for handlandmark in results.multi_hand_landmarks:
            for id,lm in enumerate(handlandmark.landmark): 
                # Get finger joint points
                h,w,_ = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy]) 
            mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)

    if lmList != []:
        #getting the value at a point
                        #x      #y
        x0,y0 = lmList[0][1],lmList[0][2]  
        x12,y12 = lmList[12][1],lmList[12][2]  
        x4,y4 = lmList[4][1],lmList[4][2]
        x17,y17 = lmList[17][1],lmList[17][2]
        x8,y8 = lmList[8][1],lmList[8][2]
        x12,y12 = lmList[12][1],lmList[12][2]
        x20,y20 = lmList[20][1],lmList[20][2]
        x9,y9 = lmList[9][1],lmList[9][2]
        x16,y16 = lmList[16][1],lmList[16][2]
        x13,y13 = lmList[13][1],lmList[13][2]
        x5,y5 = lmList[5][1],lmList[5][2]


        
        PP1 =int( hypot(x4-x12,y4-y12)) 
        PP2 = int(hypot(x20-x12,y20-y12))
        PP3 =int( hypot(x0-x12,y0-y12))
        PP4 =int( hypot(x4-x17,y4-y17))

        PP5 =int( hypot(x8-x5,y8-y5))
        PP6 =int( hypot(x12-x0,y12-y0))   
        PP7 =int( hypot(x4-x9,y4-y9))
        PP8 =int( hypot(x20-x0,y20-y0))
        PP9 =int( hypot(x16-x13,y16-y13))

        PP10 =int( hypot(x12-x9,y12-y9))
        # PP11 =int( hypot(x4-620,y4-250))

        PP12 =int( hypot(x4-310,y4-500))
        PP13 =int( hypot(x4-310,y4-0))



        
        #PLAY AND PAUSE
        if  PP1 > 130 and PP2 > 80 and PP3 > 200 and PP4>110 and PP10>90:
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(1.5)
            continue

        #Zoomin Zoom out
        if PP6<130 and  PP7<50 and  PP9<45:
            if PP5<45 and  PP8<130:
                with keyboard.pressed(Key.ctrl):
                  keyboard.press('=')
                  keyboard.release('=')
                  time.sleep(0.75)
            elif PP5>75 and  PP8>130:
                with keyboard.pressed(Key.ctrl):
                     keyboard.press('-')
                     keyboard.release('-') 
                     time.sleep(0.75)
            continue

        #Left Right '''SHIV ANNA GROUP'''

        if     PP8<140  and  PP7<40 :
            
            if PP5>65 and PP10>80:
                #LEFT
                keyboard.press(Key.left)
                keyboard.release(Key.left)
                time.sleep(1)
            Continue

            

        
        # UP DOWN

        # if  PP6<130 and  PP9<35 and PP8<125 and PP5<180 and PP7>85:
        if  PP10<60 and PP5<50 and PP6<140 and PP8<120:
            if PP12>PP13:
                #UP
                # print("Shivsagar")
                keyboard.press(Key.up)
                keyboard.release(Key.up)
                time.sleep(0.3)
            else :
                #DOWN
                # print("Niyam")
                keyboard.press(Key.down)
                '''SHIV ANNA GROUP'''
                keyboard.release(Key.down)
                time.sleep(0.3)
            continue


    # img = '''SHIV ANNA GROUP'''cv.resize(img, (412,333), interpolation=cv.INTER_CUBIC)
    cv.imshow('Image',img) #Show the video 
    if cv.waitKey(1) & 0xff==ord('q'): #By using spacebar delay will stop
        break
        
cap.release()     #stop cam       
cv.destroyAllWindows() #close window