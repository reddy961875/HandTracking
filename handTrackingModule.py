from ctypes.wintypes import RGB
from pdb import main

import cv2
import mediapipe as mp
import time

##import pTime as pTime

from main import img, mpHands, hands


class handDetection():
    def __int__(self,mode=False ,maxHands = 2, detectionCon =0.5,trackCon=0.5):
        self.mode =mode
        self.maxHands =maxHands
        self.detection =detectionCon
        self.trackCon =trackCon

        self.mpHands =mp.solutions.hands
        self.hands  =self.mpHands.Hands(self.mode,self.maxHands,self.detection,self.trackCon)
        ##self.mpDraw =mp.solutions.drawing_utils

        return img
    def findPosition(selfself, img, handNo =0 ,draw = True):
        lmList =[]

def findHands(self, img, draw = True, pTime=None):
   imageRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
   results = hands.process(imageRGB)
  ## print(results.multi_hand_landmarks)
   if results.multi_hand_landmarks:
       for handLms in results.multi_hand_landmarks:

           for id,lm in enumerate(handLms.landmark):
           ##print(id,lm)
           ##  h,w,c = img.shape
           ##  cx,cy =int(lm.x*w), int(lm.y*h)
           ##  print(id,cx,cy)
           ##  if id ==0:
           ##      cv2.circle(img,(cx,cy), 25,(255,0,255),cv2.FILLED)
           return lmList

           self.mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

       ## mp_face_mesh = mp.solutions.face_mesh

       cTime =time.time()
       fps =1/(cTime-pTime)
       pTime=cTime

       cv2.putText(img,str(int(fps)), (10,70),cv2.FONT_HERSHEY_PLAIN,3, (255,0,255),3)

   return lmList


   cv2.imshow("Image", img)
   cv2.waitKey(1)

   def main():
       pTime = 0
       cTime = 0
       cap = cv2.VideoCapture(1)
       detector = handDetector

       while True:
           success, img = cap.read( )
           img = detector.findHands(img)


   cTime = time.time()
   fps = 1 / (cTime - pTime)
   pTime = cTime

   cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
   cv2.imshow("Image", img)
   cv2.waitKey(1)

if __name__ == "__main__":
    main()
