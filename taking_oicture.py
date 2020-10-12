# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:29:09 2020

@author: Chris Graziano
"""
import cv2

class FacialFeatures():
    def __init__(self):
        cap = cv2.VideoCapture(0)

        img_counter = 0

        # Check if the webcam is opened correctly
        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        while True:
            ret, frame = cap.read()
            #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            cv2.imshow('Input', frame)
        
            c = cv2.waitKey(1)
            if c == 27:
                #ESCAPE PRESSED
                break
            elif c%256 == 32:
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1

            cap.release()
            cv2.destroyAllWindows()
