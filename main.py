import cv2
from cvzone.HandTrackingModule import HandDetector
import os
import time
detector=HandDetector(maxHands=2,detectionCon=0.8)
folder='images'
slide=sorted(os.listdir(folder),key=len)
feed=cv2.VideoCapture(0)
imageN=0
w,h=5,5
feed.set(3,w)
feed.set(4,h)

while True:
    success,img=feed.read()
    fullpath = os.path.join(folder, slide[imageN])
    image = cv2.imread(fullpath)
    image=cv2.resize(image,(1080,760))
    hands,img= detector.findHands(img)
    if hands:
        hand=hands[0]
        fingers=detector.fingersUp(hand)
        try:
            if fingers[0]==1 and fingers[1]==1:
                imageN = imageN+1
                time.sleep(1)
            else:
                imageN=imageN
        except:
            print('process finished')


    cv2.imshow('image1',image)
    cv2.imshow('image2',img)
    cv2.waitKey(1)

