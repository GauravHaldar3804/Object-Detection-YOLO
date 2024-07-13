from ultralytics import YOLO
import cv2 as cv
import cvzone
import math
import torch
import PokerHandFunction


# Check for GPU availability
if torch.cuda.is_available():
    print("YOLOv8 is running on GPU!")
else:
    print("YOLOv8 is running on CPU.")

cap = cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
# cap = cv.VideoCapture("Chapter 6 Webcam YOLO/Videos/cars.mp4")




classNames = ['10C', '10D', '10H', '10S'
              , '2C', '2D', '2H', '2S'
              , '3C', '3D', '3H', '3S'
              , '4C', '4D', '4H', '4S'
              , '5C', '5D', '5H', '5S'
              , '6C', '6D', '6H', '6S'
              , '7C', '7D', '7H', '7S'
              , '8C', '8D', '8H', '8S'
              , '9C', '9D', '9H', '9S'
              , 'AC', 'AD', 'AH', 'AS'
              , 'JC', 'JD', 'JH', 'JS'
              , 'KC', 'KD', 'KH', 'KS'
              , 'QC', 'QD', 'QH', 'QS']

model = YOLO("Project-4 Poker Hand Detection/pokerDetect.pt")

while True:
    succes , img = cap.read()
    # img = cv.flip(img,1)
    results = model(img,stream=True)
    hand = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1 , y1 , x2 , y2 = box.xyxy[0]
            x1 , y1 , x2 , y2 = int(x1) , int(y1) , int(x2) , int(y2) 
            cv.rectangle(img,(x1,y1),(x2,y2),(255,0,255),1)

            #Confidence
            conf = math.ceil(box.conf[0]*100) / 100
            # Class Names
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if conf>0.5:
                hand.append(currentClass)
            if len(hand)==5:
                results = PokerHandFunction.findHands(hand)
                cvzone.putTextRect(img,f"{results}",(300,75),scale=3,thickness=6,offset=3)

            cvzone.putTextRect(img,f"{currentClass} {conf}",(max(0,x1),max(35,y1)),scale=1,thickness=2,offset=3)
            
    cv.imshow("Webcam",img)
    cv.waitKey(1)

