#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import dlib
import sys
import pandas as pd
import os
from multiprocessing import Pool


def func(path_dir):
    inpath,outpath = path_dir.split()
    print(inpath)
    
    img = cv2.imread(inpath)
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    empty_array = np.empty((0, 2), int)
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
            empty_array = np.append(empty_array,np.array([[x,y]]), axis = 0)
            # Draw a circle
            cv2.circle(img=img, center=(x, y), radius=3, color=(0,
            255, 0), thickness=-1)


    # In[ ]:

    # show the image
    #cv2.imshow(winname="Face", mat=img)
    # Delay between every fram
    #cv2.waitKey(delay=0)
    # Close all windows
    #cv2.destroyAllWindows()


    # In[ ]:


    print(empty_array)
    #pd.DataFrame(np_array).to_csv("path/to/file.csv")np.savetxt("foo.csv", empty_array, delimiter=",")

    # In[ ]:
    pd.DataFrame(empty_array, columns=["x","y"]).to_csv(outpath)


    #empty_array.reshape(-1, 2)


    # In[ ]:
    #empty_array.zscore()


    # In[ ]:
    
if __name__ == '__main__':
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(r"shape_predictor_68_face_landmarks.dat")
    files = os.listdir("/scratch/thakrarc/senior_design/sample_face")
    pool_size = len(files)
    args = []
    for filename in files:
        path =os.path.join(r"/scratch/thakrarc/senior_design/sample_face",filename)+" "+ os.path.join(r"/scratch/thakrarc/senior_design/csv_files",filename.replace(".jpg",".csv"))
        args.append(path)
        #print(path)
        func(path)
    with Pool(pool_size) as p:
        p.map(func,args)
    p.join()
        


