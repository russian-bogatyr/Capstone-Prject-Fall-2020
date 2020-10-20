import os
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import math





#get_ipython().run_line_magic('matplotlib', 'notebook')
def calculate_ratios():
    #TO_DO 
    #Change file path
    filepath = r"F:\coding-interview\Machine-Learning-Nose-Jobs\csv_files"
    feature = pd.DataFrame(columns =["File","Delta x","Delta y","dy/dx"])
    ratios = np.array([])

    for filename in os.listdir(filepath):
        if ".csv" in filename:

            data = pd.read_csv(os.path.join(filepath,filename))

            if data.empty==False:


            
                #GOlDEN RATIO IS USED
                dx = (data.loc[16]["x"]-data.loc[0]["x"])/(data.loc[16]["x"]-data.loc[42]["x"])
                # Facial width to inner eye
                
                
                dy = (data.loc[8]["y"]-data.loc[27]["y"])/(data.loc[8]["y"]-data.loc[64]["y"])
                #Eyes to mouth to chin
            
                feature = feature.append({'File' :filename, 'Delta x' : dx, 'Delta y' : dy},  
                        ignore_index = True) 
                ratios = np.append(ratios, ([dx, dy]) , axis = 0)

                final_ratios = np.reshape(ratios,(-1,2))
         

    #remove plot
    y = feature["Delta y"].to_numpy()
    x = feature["Delta x"].to_numpy()
    plt.plot(x,y,"o",alpha=0.2)
    plt.show()
    #remove above
    return final_ratios

def calculate_ratio(facial_coordinates):
    empty_ar = np.array([])
    x = (facial_coordinates[16][0] - facial_coordinates[0][0]) / (facial_coordinates[16][0] - facial_coordinates[42][0])
    
    y = (facial_coordinates[8][1] - facial_coordinates[27][1]) / (facial_coordinates[8][1] - facial_coordinates[64][1]) 
    empty_ar = np.append(empty_ar, (x, y), axis = 0)
    final_ratio = np.reshape(empty_ar, (-1, 2))
    #remove plot
    plt.plot(x, y, 'r*')
    return (final_ratio)
