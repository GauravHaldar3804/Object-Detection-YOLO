from ultralytics import YOLO
import cv2 as cv
import cvzone
import math
import torch


# Check for GPU availability
if torch.cuda.is_available():
    print("YOLOv8 is running on GPU!")
else:
    print("YOLOv8 is running on CPU.")

# cap = cv.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)
cap = cv.VideoCapture("Chapter 6 Webcam YOLO/Videos/ppe-1-1.mp4")



myColor = (0,0,255)
classNames = ['Hardhat','Mask','NO-Hardhat','NO-Mask','NO-Safety Vest','Person','Safety Cone','Safety Vest','machinery','vehicle']

model = YOLO("Project-3 ppe detection/ppe.pt")

while True:
    succes , img = cap.read()
    img = cv.flip(img,1)
    results = model(img,stream=True)

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
            if conf > 0.5:
                if currentClass == "Hardhat" or currentClass == "Mask" or currentClass == "Safety Vest":
                    myColor = (0,255,0)
                elif currentClass == "NO-Hardhat" or currentClass == "NO-Mask" or currentClass == "NO-Safety Vest":
                    myColor = (0,0,255)
                else :
                    myColor = (255,0,255)
                    

                cvzone.putTextRect(img,f"{currentClass} {conf}",(max(0,x1),max(35,y1)),scale=1,thickness=2,offset=3,colorR=myColor)
                cv.rectangle(img,(x1,y1),(x2,y2),myColor,1)

    cv.imshow("Webcam",img)
    cv.waitKey(1)

