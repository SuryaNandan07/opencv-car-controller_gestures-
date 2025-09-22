import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import pyautogui as pg
import random
import time
from pynput.keyboard import Key, Controller

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
imgSize = 3000
offset = 20

keyboard = Controller()
#
time.sleep(10)

""""""
while True:

    success, img = cap.read()
    hands, img = detector.findHands(img)
    cv2.waitKey(1)
    keyboard.press('w')
    '''if hands:
        hand = hands[0]
        x,y,w,h=hand['bbox']
        imgWhite=np.ones((imgSize,imgSize,3),np.uint8)*255

        imgCrop = img[y-offset:y+h+offset,x-offset:x+w+offset]
        imgCropShape=imgCrop.shape
        imgWhite[0:imgCropShape[0],0:imgCropShape[1]]=imgCrop
        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)'''
    # keyboard.press('w')

    hands, img = detector.findHands(img)
    if hands:
        # keyboard.press('w')

        handType = hands[0]['type']  # 'Left' or 'Right'
        print("Detected:", handType)
        if handType == 'Right':
            # print("--->")
            keyboard.press('d')
            # keyboard.press('w')

            # time.sleep(0.2)
            # keyboard.release('d')

            # pg.press('enter')
        else:
            # print("<---")
            # pg.write("Idly"+i)
            keyboard.press('a')
            # keyboard.press('w')

            # time.sleep(0.2)
            # keyboard.release('a')

            # pg.press('enter')
        # keyboard.press('w')
    else:
        keyboard.release('d')
        keyboard.release('a')

    cv2.imshow("Image", img)
    cv2.waitKey(1)