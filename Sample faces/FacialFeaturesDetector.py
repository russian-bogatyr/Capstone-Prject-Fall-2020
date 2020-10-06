#!/usr/bin/env python
# coding: utf-8
import cv2
import numpy as np
import dlib
import random
import os

# Load the detector
detector = dlib.get_frontal_face_detector()

filename = random.choice(os.listdir(os.curdir))
# Load the predictor
predictor = dlib.shape_predictor(r"shape_predictor_68_face_landmarks.dat")

# read the image
img = cv2.imread(os.path.join(os.curdir, filename))

# Convert image into grayscale
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

# # Jaw Points = 0–16
# # Right Brow Points = 17–21
# # Left Brow Points = 22–26 
# # Nose Points = 27–35
# # Right Eye Points = 36–41
# # Left Eye Points = 42–47
# # Mouth Points = 48–60
# # Lips Points = 61–67

# Use detector to find landmarks
empty_array = np.array([])
faces = detector(gray)
for face in faces:
    #x1 = face.left() # left point
    #y1 = face.top() # top point
    #x2 = face.right() # right point
    #y2 = face.bottom() # bottom point
    # Create landmark object
    landmarks = predictor(image=gray, box=face)
    # Loop through all the points
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y        
        empty_array = np.append(empty_array, [x, y] , axis = 0)
        # Draw a circle
        cv2.circle(img=img, center=(x, y), radius=3, color=(0,
        255, 0), thickness=-1)

# show the image
cv2.imshow(winname="Face", mat=img)
# Delay between every fram
cv2.waitKey(delay=0)
# Close all windows

#cv2.destroyAllWindows()
print(empty_array)
empty_array.reshape(-1, 2)


