# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:29:09 2020

@author: Chris Graziano and Tony
"""

import cv2
import numpy as np
import dlib

class FacialFeatures():
    def getCoords(pat):
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(r"shape_predictor_68_face_landmarks.dat")
        #placeholder, should crate class for uploading picture
        gray = cv2.cvtColor(src=pat, code=cv2.COLOR_BGR2GRAY)
        # Use detector to find landmarks
        facialPoints = np.array([])
        faces = detector(gray)    
        for face in faces:
            # Create landmark object
            landmarks = predictor(image=gray, box=face)
            # Loop through all the points
            for n in range(0, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y        
                facialPoints = np.append(facialPoints, ([x, y]) , axis = 0)
                # Draw a circle
                cv2.circle(img=pat, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1)
                
                #show the image
                #cv2.imshow(winname=\"Face\", mat=img)
                # Delay between every fram
                #cv2.waitKey(delay=0)
                # Close all windows
                #cv2.destroyAllWindows()
                

        return np.reshape(facialPoints, (-1, 2))
    
        
