# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:49:18 2020

@author: Computer
"""



def eye_distance(landmarks):

    head_left = landmarks.part(0).x
    head_right = landmarks.part(16).x
    

    eye_left = landmarks.part(39).x
    
    eye_right = landmarks.part(42).x
    
    ratio = (head_right-head_left)/(eye_right-eye_left)
    
    return ratio
    
import cv2
import dlib


pics = ["joel_near_straight.jpg", "joel_near_tilt.jpg", "joel_near_turn.jpg",
        "joel_mid_straight.jpg", "joel_mid_tilt.jpg", "joel_mid_turn.jpg",
        "joel_far_straight.jpg", "joel_far_tilt.jpg", "joel_far_turn.jpg"]

for pic in pics:    
    img = cv2.imread(pic)
    
    scale_percent = 60 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (30,30)
    fontScale              = 1
    fontColor              = (0,0,0)
    lineType               = 2
    
    
    
     
    """
    
    cv2.imshow(winname = "Face", mat = img)
    
    cv2.waitKey(delay =0)
    
    cv2.destroyAllWindows()
    """
    
    pics = ["joel_near_straight.jpg", "joel_near_tilt.jpg", "joel_near_turn.jpg",
            "joel_mid_straight.jpg", "joel_mid_tilt.jpg", "joel_mid_turn.jpg",
            "joel_far_straight.jpg", "joel_far_tilt.jpg", "joel_far_turn.jpg"]
    
    
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    
    gray = cv2.cvtColor(src = img, code = cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)
    
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        
        # Drawas a box arround face.
        #cv2.rectangle(img = img, pt1 =(x1, y1), pt2=(x2, y2), color = (0,255,0), thickness = 4)
    
        # Look for the landmarks
        landmarks = predictor(image=gray, box=face)
        for n in range(landmarks.num_parts):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            text = str(eye_distance(landmarks))
            # Draw a circle
            cv2.circle(img=img, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1)
    
    
    
    cv2.putText(img,text, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    
    cv2.imshow(winname = "Face", mat = img)
    
    cv2.waitKey(delay =0)
    
    cv2.destroyAllWindows()
    

















