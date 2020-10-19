# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:29:09 2020

@author: Chris Graziano
"""
import cv2
class TakePicture:
    def __init__(self):
        cap = cv2.VideoCapture(0)

        img_counter = 0

        # Check if the webcam is opened correctly
        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        while True:
            ret, frame = cap.read()
            #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            cv2.imshow('Press Space to take a picture. Press Esc to exit.', frame)

            c = cv2.waitKey(1)
            if c == 27:
                #ESCAPE PRESSED
                break
            if c%256 == 32:
                # SPACE pressed
                self.patient = frame
                img_counter += 1
                break
        cap.release()
        cv2.destroyAllWindows()
    def getPatientFace(self):
        return self.patient