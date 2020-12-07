#!/usr/bin/env python
# coding: utf-8

# In[19]:


import cv2
import numpy as np
import pandas as pd
import dlib
import sys
import os

detector = dlib.get_frontal_face_detector()

predictor68 = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
nasal_type = {}

def nasalIndex(height, width):
    return (width*100)/height


def defineCluster(facial_coordinates,file_name):
    nasal_type[file_name] = {}
    #method to calulate nasal index and define its cluster
    height_of_nose = euclidean_distance(facial_coordinates.loc[27]["Y"], 
                                        facial_coordinates.loc[34]["Y"])
    width_of_nose  = euclidean_distance(facial_coordinates.loc[138]["X"], 
                                        facial_coordinates.loc[148]["X"])
    nasal_index = nasalIndex(height_of_nose,width_of_nose)
    #if(nasal_index <= 39.99):
    #    nasal_type[file_name]["Overly narrow nose"] = nasal_index
    #    print("Overly narrow nose")
    if(nasal_index <= 54.99):
        nasal_type[file_name]['Very and Overly narrow nose'] = nasal_index
        print('Very narrow nose')
    elif(nasal_index <= 69.99):
        nasal_type[file_name]['Narrow nose'] = nasal_index
        print('Narrow nose')
    elif(nasal_index <= 84.99):
        nasal_type[file_name]['Medium nose'] = nasal_index
        print('Medium nose')
    elif(nasal_index <= 99.99):
        nasal_type[file_name]['Broad and very broad nose'] = nasal_index
        print('Broad nose') 
    #elif(nasal_index <= 114.99):
    #    nasal_type[file_name]['Very broad nose'] = nasal_index
   
   #print('Very broad nose')
    else:
        nasal_type[file_name]["Overly broad nose"] = nasal_index
        print("Overly broad nose")



def extract_point(filepath):
    file_tocsv = r"./csv_files"
    
    img = cv2.imread(filepath)

    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    
    
    
    faces = detector(gray)
    for face in faces:
        landmarks68 = predictor68(image=gray, box=face)
    
        array_68 = np.matrix([[p.x, p.y] for p in landmarks68.parts()])
        
        #print(array_68)
        face_cord_68 = pd.DataFrame(array_68, columns = ['X', 'Y'])
        face_cord_68.to_csv(os.path.join(file_tocsv,filepath.split(os.path.sep)[-1].replace(".jpg",".csv")))
        '''
        array_194 = np.matrix([[q.x, q.y] for q in landmarks194.parts()])
        ind = np.array(range(0,array_194.shape[0]))
        ind = np.reshape(ind,(array_194.shape[0],1))  
        array_194 = np.concatenate((array_194, ind), axis=1) 
        face_cord_194 = pd.DataFrame(array_194, columns = ['X', 'Y'])
        '''
        '''
        x1 = face.left() # left point
        y1 = face.top() # top point
        x2 = face.right() # right point
        y2 = face.bottom() # bottom point
        # Create landmark object
        landmarks68 = predictor68(image=gray, box=face)
        landmarks194 = predictor194(image=gray, box=face)
        
        
        array_68 = np.matrix([[p.x, p.y] for p in landmarks68.parts()])
        ind = np.array(range(0,array_68.shape[0]))
        ind = np.reshape(ind,(array_68.shape[0],1))  
        array_68 = np.concatenate((array_68, ind), axis=1) 
        face_cord_68 = pd.DataFrame(array_68, columns = [ 'X', 'Y','Point index'])
        face_cord_68.to_csv(os.path.join(file_tocsv,name.replace(".csv","_68.csv")),index=False)
        print(face_cord_68.shape)
        
        array_194 = np.matrix([[q.x, q.y] for q in landmarks194.parts()])
        ind = np.array(range(0,array_194.shape[0]))
        ind = np.reshape(ind,(array_194.shape[0],1))  
        array_194 = np.concatenate((array_194, ind), axis=1) 
        face_cord_194 = pd.DataFrame(array_194, columns = ['X', 'Y','Point index'])
        face_cord_194.to_csv(os.path.join(file_tocsv,name.replace(".csv","_194.csv")),index=False)
        print(face_cord_194.shape)
        #print(points_68.shape)
        #points_68 = np.array(points_68)
        #ind = np.array(range(0,points_68.shape[0]))
        #ind = np.reshape(ind,(points_68.shape[0],1))  
        #print(points_68)
        #points_68 = np.concatenate((points_68, ind), axis=1) 
        #points_194 = np.array(landmarks194.parts())
        
        
        
        ind = np.array(range(0,points_194.shape[0]))
        ind = np.reshape(ind,(points_68.shape[0],1))  
        points_194 = np.concatenate((points_68, ind), axis=1) 
        print("68 MARKERS ",landmarks68.parts())
        print("164 MARKERS ",landmarks194.parts())
        '''
        
        '''
        for n in range(0,69):
            x_1 = landmarks68.part(n).x
            y_1 = landmarks68.part(n).y              
            empty_array_68.append((n, x_1, y_1 ))
            #empty_array_164.append((n, x, y ))
            # Draw a circle
            #cv2.circle(img=img, center=(x, y), radius=3, color=(0,255, 0), thickness=-1)
        '''
    # show the image
    #cv2.imshow(winname="Face", mat=img)
    # Delay between every fram
    #cv2.waitKey(delay=0)
    # Close all windows
    #cv2.destroyAllWindows()

    
    #print(face_cord)
    #face_cord = pd.DataFrame(empty_array_68, columns = [ 'Delta X', 'Delta Y','Point index'])
    #face_cord = face_cord.set_index(points)
    #face_cord.to_csv(os.path.join(file_tocsv,name),index=False)
    #defineCluster(face_cord,filepath.split("/")[-1])
    
    
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1-point2)**2))
    
count =0
path_to_images = r"./dataset_3"
for filename in os.listdir(path_to_images):
    file_dir = os.path.join(path_to_images,filename)
    extract_point(file_dir)
    count = count +1

#print(nasal_type)    

#FILE WRITE

'''
with open(r"dist.csv","w") as fil:
    fil.write("File,Cat,val\n")
    for outter in nasal_type.items():
        for inner in outter[1].items():
            fil.write(str(outter[0])+","+str(inner[0])+","+str(inner[1])+"\n")
'''
#    for it in nasal_type.items():
#        fil.write(str(it[0])+","+str(str(it[1]))+"\n")

    

# In[93]:




# In[94]:


#



# In[95]:


#face_cord


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


#createNosePoints(face_cord)


# In[ ]: