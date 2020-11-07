#!/usr/bin/env python
# coding: utf-8

# In[19]:


import cv2
import numpy as np
import pandas as pd
import dlib
import sys


# In[20]:


# Load the detector
detector = dlib.get_frontal_face_detector()


# In[21]:


predictor68 = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
predictor194 = dlib.shape_predictor('shape_predictor_194_face_landmarks.dat')


# In[22]:


img = cv2.imread('TestImages/image_2.jpg')


# In[23]:


gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)


# In[62]:


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
        if(n == 27 or n == 28 or n == 29 or n ==30 or n ==32 or n == 33 or n ==34):
            x = landmarks68.part(n).x
            y = landmarks68.part(n).y        
            empty_array.append((n, x, y ))
            # Draw a circle
            cv2.circle(img=img, center=(x, y), radius=3, color=(0,
            255, 0), thickness=-1)
        
        
    for n in range(135,152):
        if(n == 135 or n == 138 or n ==148 or n ==151):
            x = landmarks194.part(n).x
            y = landmarks194.part(n).y        
            empty_array.append((n, x, y))
            # Draw a circle
            cv2.circle(img=img, center=(x, y), radius=3, color=(0,
            255, 0), thickness=-1)   


# In[63]:


# show the image
cv2.imshow(winname="Face", mat=img)
# Delay between every fram
cv2.waitKey(delay=0)
# Close all windows
cv2.destroyAllWindows()


# In[64]:


face_cord = pd.DataFrame(empty_array, columns = ['Point index', 'X', 'Y'])
print(face_cord)


# In[27]:


def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1-point2)**2))


# In[92]:


def defineCluster(facial_coordinates):
    #method to calulate nasal index and define its cluster
    height_of_nose = euclidean_distance(facial_coordinates.loc[0]["Y"], 
                                        facial_coordinates.loc[6]["Y"])
    width_of_nose  = euclidean_distance(facial_coordinates.loc[8]["X"], 
                                        facial_coordinates.loc[9]["X"])
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


# In[93]:


def nasalIndex(height, width):
    return (width*100)/height


# In[94]:


defineCluster(face_cord)


# In[95]:


face_cord


# In[96]:


def createNosePoints(face_cord):
    # method to create new points 152 - 155
    new_points = []
    def calculateMidDistance(point1, point2):
        return ((point1+point2)/2) 
    x = face_cord.loc[4]["X"]
    y = face_cord.loc[3]["Y"]
    new_points.append((152, x, y))
    
    x = face_cord.loc[6]["X"]
    y = face_cord.loc[3]["Y"]
    new_points.append((153, x, y))
    
    x = face_cord.loc[3]["X"]
    y = calculateMidDistance(face_cord.loc[1]["Y"], face_cord.loc[2]["Y"])
    new_points.append((154, x, y))
    
    x = face_cord.loc[6]["X"]
    y = calculateMidDistance(face_cord.loc[1]["Y"], face_cord.loc[2]["Y"])
    new_points.append((155, x, y))
    
    new_nose_cords = pd.DataFrame(new_points, columns= ['Point index', 'X', 'Y'])
    new_face_cords = face_cord.append(new_nose_cords, ignore_index = True)
    return new_face_cords


# In[97]:


createNosePoints(face_cord)


# In[ ]:




