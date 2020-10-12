# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:15:54 2020

@author: tony
"""

import cv2
import numpy as np
import sys
import os
import random
import dlib

class FacialFeatures:
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(r"shape_predictor_68_face_landmarks.dat")
    #placeholder, should crate class for uploading picture
    os.chdir(os.path.join(os.path.dirname(os.curdir), 'Sample faces'))
    img = cv2.imread(random.choice(os.listdir(os.curdir)))
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    # Use detector to find landmarks
    facial_points = np.array([])
    faces = detector(gray)    
    for face in faces:
        x1 = face.left() # left point
        y1 = face.top() # top point
        x2 = face.right() # right point
        y2 = face.bottom() # bottom point
        # Create landmark object
        landmarks = predictor(image=gray, box=face)
        # Loop through all the points
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y        
            facial_points = np.append(facial_points, ([x, y]) , axis = 0)
            # Draw a circle
            cv2.circle(img=img, center=(x, y), radius=3, color=(0,
            255, 0), thickness=-1)

    #show the image
    #cv2.imshow(winname=\"Face\", mat=img)
    # Delay between every fram
    #cv2.waitKey(delay=0)
    # Close all windows
    #cv2.destroyAllWindows()
    facialCords = np.reshape(facial_points, (-1, 2))  
    def calculateFacialSize(facialCords):
        width = facialCords[16][0] - facialCords[0][0] # top right(17) - top left(1)
        height = facialCords[8][1] - facialCords[27][1] # bottom center(9) - top center(28)
        #print(width, height)
        return (width , height)
    #calculateFacialSize(facial_coordinates)

