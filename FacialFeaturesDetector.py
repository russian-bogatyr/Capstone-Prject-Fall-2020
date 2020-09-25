#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import dlib
import sys


# In[ ]:


# Load the detector
detector = dlib.get_frontal_face_detector()


# In[ ]:


# Load the predictor
predictor = dlib.shape_predictor(r"C:\Users\Anton\Desktop\FALL 2020\CS490 (SE450)\Detect-Facial-Features-master\Detect-Facial-Features-master\shape_predictor_68_face_landmarks.dat")


# In[ ]:


# read the image
img = cv2.imread(r"C:\Users\Anton\Desktop\FALL 2020\CS490 (SE450)\Detect-Facial-Features-master\Detect-Facial-Features-master\images\image_2.jpg")


# In[ ]:


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
# 

# In[ ]:


# Use detector to find landmarks
empty_array = np.array([])
faces = detector(gray)
for face in faces:
    x1 = face.left() # left point
    y1 = face.top() # top point
    x2 = face.right() # right point
    y2 = face.bottom() # bottom point
    # Create landmark object
    landmarks = predictor(image=gray, box=face)
    # Loop through all the points
    for n in range(0, 27):
        x = landmarks.part(n).x
        y = landmarks.part(n).y        
        empty_array = np.append(empty_array, ([x, y]) , axis = 0)
        # Draw a circle
        cv2.circle(img=img, center=(x, y), radius=3, color=(0,
        255, 0), thickness=-1)


# In[ ]:


# show the image
cv2.imshow(winname="Face", mat=img)
# Delay between every fram
cv2.waitKey(delay=0)
# Close all windows
cv2.destroyAllWindows()


# In[ ]:


print(empty_array)


# In[ ]:


empty_array.reshape(-1, 2)


# In[ ]:


empty_array.zscore()


# In[ ]:




