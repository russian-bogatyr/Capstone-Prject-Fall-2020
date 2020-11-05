# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:29:09 2020

@author: Chris Graziano and Tony
"""
import os
import pandas as pd
import numpy as np

#get_ipython().run_line_magic('matplotlib', 'notebook')
def calculate_ratios():
    #TO_DO
    #Change file path
    #os.chdir(os.path.join(os.path.dirname(os.curdir), 'csv_files'))
    filepath = r"./csv_files"
    feature = pd.DataFrame(columns =["File","Delta x","Delta y","dy/dx"])
    #filepath = r"csv_files"

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



    #remove plot

    # y = feature["Delta y"].to_numpy()
    # x = feature["Delta x"].to_numpy()
    # plt.plot(x,y,"o",alpha=0.2)
    # plt.show()
    # #remove above

    #feature.to_csv("golden_ratio.csv")
    return feature




def calculate_ratio(facial_coordinates):
    empty_ar = np.array([])

    x = (facial_coordinates[16][0] - facial_coordinates[0][0]) / (facial_coordinates[16][0] - facial_coordinates[42][0])
    y = (facial_coordinates[8][1] - facial_coordinates[27][1]) / (facial_coordinates[8][1] - facial_coordinates[64][1])
    final_ratio = np.reshape(empty_ar, (-1, 2))
    final_ratio = np.append(empty_ar, (x, y), axis = 0)
    #final_ratio = np.reshape(empty_ar, (-1, 2))
    # remove plot
    # plt.plot(x, y, 'r*')
    return (final_ratio)
calculate_ratios()
