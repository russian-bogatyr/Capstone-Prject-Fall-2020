#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import pandas as pd
import dlib
import sys


# In[2]:


# Load the detector
detector = dlib.get_frontal_face_detector()


# In[3]:


predictor68 = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
predictor194 = dlib.shape_predictor('shape_predictor_194_face_landmarks.dat')


# In[4]:


img = cv2.imread('TestImages/image_7.jpg')


# In[5]:


gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)


# In[6]:


empty_array = []
faces = detector(gray)
for face in faces:
    x1 = face.left() # left point
    y1 = face.top() # top point
    x2 = face.right() # right point
    y2 = face.bottom() # bottom point
    # Create landmark object
    landmarks68 = predictor68(image=gray, box=face)
    landmarks194 = predictor194(image=gray, box=face)
    # Loop through all the points
    
    #for 194 nose points are 135, 152
    #for 68 nose points are 27, 36
    for n in range(27, 36):
        x = landmarks68.part(n).x
        y = landmarks68.part(n).y        
        empty_array.append((n, x, y ))
        # Draw a circle
        cv2.circle(img=img, center=(x, y), radius=3, color=(0,
        255, 0), thickness=-1)
    for n in range(135,152):
        x = landmarks194.part(n).x
        y = landmarks194.part(n).y        
        empty_array.append((n, x, y))
        # Draw a circle
        cv2.circle(img=img, center=(x, y), radius=3, color=(0,
        255, 0), thickness=-1)   


# In[7]:


# show the image
cv2.imshow(winname="Face", mat=img)
# Delay between every fram
cv2.waitKey(delay=0)
# Close all windows
cv2.destroyAllWindows()


# In[130]:


face_cord = pd.DataFrame(empty_array, columns = ['Point index', 'X', 'Y'])
print(face_cord)


# In[131]:


def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1-point2)**2))


# In[132]:


def defineCluster(facial_coordinates):
    #height_of_nose = euclidean_distance(facial_coordinates[0], facial_coordinates[6])
    #top_cord = facial_coordinates.loc[0]["Y"]
    #bottom_cord = facial_coordinates.loc[6]["Y"]
    height_of_nose = euclidean_distance(facial_coordinates.loc[0]["Y"], facial_coordinates.loc[6]["Y"])
    width_of_nose  = euclidean_distance(facial_coordinates.loc[12]["X"], facial_coordinates.loc[22]["X"])
    nasal_index = nasalIndex(height_of_nose,width_of_nose)
    if(nasal_index <= 39.99):
        print("Overly narrow nose")
    elif(nasal_index <= 54.99):
        print('Very narrow nose')
    elif(nasal_index <= 69.99):
        print('Narrow nose')
    elif(nasal_index <= 84.99):
        print('Medium nose')
    elif(nasal_index <= 99.99):
        print('Broad nose') 
    elif(nasal_index <= 114.99):
        print('Very broad nose')
    else:
        print("Overly broad nose")


# In[133]:


def nasalIndex(height, width):
    return (width*100)/height


# In[134]:


defineCluster(face_cord)


# In[ ]:




