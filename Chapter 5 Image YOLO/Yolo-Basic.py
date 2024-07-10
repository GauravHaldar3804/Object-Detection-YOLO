from ultralytics import YOLO
import cv2 as cv

model = YOLO("YOLO_Weights/yolov8l.pt")
img = cv.imread("Chapter 5 Image YOLO/Images/1.jpg")
imgS = cv.resize(img , (0,0) , None , 0.2 , 0.2)
# cv.imshow("Image",img)
results = model(imgS,show = True)
cv.waitKey(0)
