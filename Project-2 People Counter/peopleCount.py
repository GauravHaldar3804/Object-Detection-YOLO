from ultralytics import YOLO
import cv2 as cv
import cvzone
import math
import torch
import numpy as np
from sort import*


# Check for GPU availability
if torch.cuda.is_available():
    print("YOLOv8 is running on GPU!")
else:
    print("YOLOv8 is running on CPU.")

# cap = cv.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)
cap = cv.VideoCapture("Chapter 6 Webcam YOLO/Videos/people.mp4")

mask = cv.imread("Project-2 People Counter/mask.png")





classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

model = YOLO("YOLO_Weights/yolov8l.pt")
currentArray = np.empty((0,5))
tracker = Sort(max_age=20)
limitsUp = [103,161,296,161]
limitsDown = [527,489,735,489]

totalCountUp = []
totalCountDown = []

graphics = cv.imread("Project-2 People Counter/Graphics.png",cv.IMREAD_UNCHANGED)

while True:
    succes , img = cap.read()
    # img = cv.flip(img,1)
    maskedImg = cv.bitwise_and(img,mask)
    results = model(maskedImg,stream=True)
    detections = np.empty((0,5))

    
     
    

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1 , y1 , x2 , y2 = box.xyxy[0]
            x1 , y1 , x2 , y2 = int(x1) , int(y1) , int(x2) , int(y2) 
            

            #Confidence
            conf = math.ceil(box.conf[0]*100) / 100
            # Class Names
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if currentClass == "person" and conf>0.3  :
                # cvzone.putTextRect(img,f"{currentClass} {conf}",(max(0,x1),max(35,y1)),scale=1,thickness=2,offset=3)
                # cv.rectangle(img,(x1,y1),(x2,y2),(0,255,0),1)
                currentArray = np.array([x1,y1,x2,y2,conf])
                detections = np.vstack((detections,currentArray))

    cv.line(img,(limitsUp[0],limitsUp[1]),(limitsUp[2],limitsUp[3]),(0,0,255),5)
    cv.line(img,(limitsDown[0],limitsDown[1]),(limitsDown[2],limitsDown[3]),(0,0,255),5)


    resultsTracker = tracker.update(detections)
    for results in resultsTracker:
        x1 , y1 , x2 , y2 , id = results
        x1 , y1 , x2 , y2 ,id = int(x1) , int(y1) , int(x2) , int(y2) , int(id)
        cv.rectangle(img,(x1,y1),(x2,y2),(0,255,0),1)
        cvzone.putTextRect(img,f"{id}",(max(0,x1),max(35,y1)),scale=2,thickness=2,offset=3)
        cx , cy = x1 +(x2-x1)//2 ,y1+(y2-y1)//2
        cv.circle(img,(cx,cy),5,(255,0,255),cv.FILLED)

        if limitsUp[0] < cx < limitsUp[2] and limitsUp[1]-20 < cy < limitsUp[1]+20:
            if totalCountUp.count(id)==0: 
                totalCountUp.append(id)
                cv.line(img,(limitsUp[0],limitsUp[1]),(limitsUp[2],limitsUp[3]),(0,255,0),5)

        if limitsDown[0] < cx < limitsDown[2] and limitsDown[1]-20 < cy < limitsDown[1]+20:
            if totalCountDown.count(id)==0: 
                totalCountDown.append(id)
                cv.line(img,(limitsDown[0],limitsDown[1]),(limitsDown[2],limitsDown[3]),(0,255,0),5)
        

    # cvzone.putTextRect(img,f"Count:{len(totalCount)}",(55,55))
    img[174:174+136,705:705+575] = graphics
    cv.putText(img ,str(len(totalCountUp)),(855,280),cv.FONT_HERSHEY_PLAIN,8,(0,255,0),8)
    cv.putText(img ,str(len(totalCountDown)),(1125,280),cv.FONT_HERSHEY_PLAIN,8,(0,0,255),8)

    cv.imshow("Webcam",img)
    # cv.imshow("Mask",maskedImg)
    cv.waitKey(1)

