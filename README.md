
# YOLO Object Detection

This repository contains multiple projects showcasing the application of YOLO (You Only Look Once) object detection. Each project demonstrates the use of YOLO for solving specific real-world problems.

## Table of Contents
1. [Introduction](#introduction)  
2. [Projects](#projects)  
   - [Project 1: Car Counting](#project-1-car-counting)  
   - [Project 2: People Counter](#project-2-people-counter)  
   - [Project 3: PPE Detection](#project-3-ppe-detection)  
   - [Project 4: Poker Hand Detection](#project-4-poker-hand-detection)  
3. [Setup Instructions](#setup-instructions)  
4. [Requirements](#requirements)  


## Introduction
YOLO is a state-of-the-art object detection algorithm that enables fast and accurate detection of objects in real time. This repository uses YOLOv4 and YOLOv8 for various projects, highlighting its versatility across different domains.

## Projects

### Project 1: Car Counting
- **Description**: Detects and counts cars in a video feed or a real-time webcam stream.  
- **Implementation**:  
  1. Pre-trained YOLOv4 weights were used to detect cars in video frames.  
  2. Each frame is processed using OpenCV to apply YOLO detection.  
  3. A bounding box is drawn around detected cars, and a counter keeps track of unique cars using object tracking techniques like centroid tracking.  
  - **Use Case**: Useful for traffic management and analysis.

### Project 2: People Counter
- **Description**: Detects and counts people in a defined area, such as public spaces or offices.  
- **Implementation**:  
  1. YOLOv4 weights trained on COCO dataset were used to identify humans in video streams.  
  2. The area of interest is defined using a virtual boundary to count people entering or leaving.  
  3. Frame processing and tracking were implemented using OpenCV and NumPy for efficient real-time performance.  
  - **Use Case**: Ideal for crowd management and monitoring occupancy levels.

### Project 3: PPE Detection
- **Description**: Detects if individuals are wearing proper personal protective equipment (PPE), such as helmets or vests.  
- **Implementation**:  
  1. A custom YOLOv8 model was trained on a dataset of images with annotations for helmets, vests, and non-compliance.  
  2. TensorFlow was used for data preprocessing and augmentation to improve model accuracy.  
  3. The model detects PPE violations in real time using video feeds or images and highlights non-compliant individuals.  
  - **Use Case**: Ensures workplace safety compliance in industries like construction and manufacturing.

### Project 4: Poker Hand Detection
- **Description**: Identifies and detects poker hands using YOLO object detection.  
- **Implementation**:  
  1. A custom dataset of poker cards was collected and annotated using tools like LabelImg.  
  2. YOLOv8 was trained to classify and detect individual cards in the hand.  
  3. The model uses OpenCV to preprocess and detect the bounding boxes, while the logic to evaluate poker hands is integrated with the detection results.  
  - **Use Case**: Useful for gaming analytics and automated card identification.

## Setup Instructions
1. Clone this repository:  
   ```bash
   git clone https://github.com/GauravHaldar3804/Object-Detection-YOLO.git
      
2.Set up a Python virtual environment

    python -m venv myvenv
    source myvenv/bin/activate   (Linux/MacOS)
    myvenv\Scripts\activate      ( Windows )
3. Install the required dependencies:

       pip install -r requirements.txt

4.Download the YOLO weights and place them in the YOLO_Weights directory.

##Requirements
Install all dependencies listed in requirements.txt. Some key libraries include:

OpenCV
PyTorch
NumPy





