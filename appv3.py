from tkinter import Tk, Label, Button, Entry,CENTER, Toplevel
from tkinter import font as tkfont
import pandas as pd
from PIL import ImageTk, Image
import csv
import random
import os
import FacialFeatureClass
import KNNalg
import ratioCompute
import UploadClass
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image 
# # loading Python Imaging Library 
# from PIL import ImageTk, Image 

# # To get the dialog box to open when required  
# from tkinter import filedialog

#choosing the face
#this will be imported in a later version of the app
#we have to navigate to Sample faces first because there are more csvs than faces.

os.chdir(os.path.join(os.path.dirname(os.curdir), 'Sample faces'))

#imageName = random.choice(os.listdir(os.curdir))
fileName = []
first40faces = []
faceFeats = []  
client_ratio = np.array([])
datastore_ratios = np.array([])
ratio_df = None
root = None
#filePath = "csv_files/"+fileName+".csv.chip.csv"

#this class organizes all of the frames

class NoseApp:
  
    global root 
    root = Tk()
       
    def upload_image_button():
        global faceFeats 
        faceFeats = UploadClass.Upload_Picture.open_img() 

    
    def start_process_button():
        global faceFeats
        global first40faces
        global ratio_df
        #below is block to check if face is uploaded
        if len(faceFeats) == 0:
            print("You didn't uplaod picture")
        else:
            client_ratio = ratioCompute.calculate_ratio(faceFeats)
            ratio_df = pd.read_csv('F:\coding-interview\Machine-Learning-Nose-Jobs\golden_ratio.csv')
            datastore_ratios = ratio_df[['Delta x','Delta y']].to_numpy()
            first40faces = KNNalg.get_neighbors(datastore_ratios, client_ratio , 5)
            
                
    def show_results_button():
        
        global root
        global fileName
        #go through each element in "element" and find file name in sample faces
        for i in range(len(first40faces)):
                  # print(first40faces[i])
                  element = ratio_df[(ratio_df["Delta x"] == first40faces[i][0]) & (ratio_df["Delta y"] == first40faces[i][1])]
                  element = element.drop(columns = ["Delta x" ,"Delta y" , "dy/dx"])
                  element["File"] = element["File"].str.replace(".csv" , ".jpg")
                  element = element["File"].to_string(index = False)
                  filePath = os.getcwd()+ "\\" + element.strip()
                  try:

                        img = Image.open(r'%s' % filePath)
                        img = img.resize((150, 150), Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        panel = Label(root, image=img)
                        panel.image = img
                        panel.pack()
                  except Exception as e:
                        print(e)
    
    #master.geometry("300x200")
    root.title("Smart Nose Surgery")
    root.geometry('400x300+%d+%d' % (root.winfo_width(), root.winfo_height()))

    upload_button = Button(root, text="Upload Image", command = upload_image_button)
    upload_button.place(relx = 0.1, rely = 0.5, anchor = CENTER)
    upload_button.pack()

    start_button = Button(root, text="Start Process",  command = start_process_button)
    start_button.place(relx = 0.2, rely = 0.5, anchor = CENTER)  
    start_button.pack()
    
    start_button = Button(root, text="Show Results",  command = show_results_button)
    start_button.place(relx = 1, rely = 0.8, anchor = CENTER)  
    start_button.pack()

    root.mainloop()
    

    
        
    


