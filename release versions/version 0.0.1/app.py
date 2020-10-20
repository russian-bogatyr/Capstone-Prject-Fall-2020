
from tkinter import Tk, Label, Button, Entry,CENTER, Toplevel
from tkinter import font as tkfont
from PIL import ImageTk, Image
import csv
import random
import os
import FacialFeatureClass
import OpenImageClass
import KNNalg
import taking_picture
import ratio_compute
import UploadClass
import numpy as np
import matplotlib.pyplot as plt
# # loading Python Imaging Library 
# from PIL import ImageTk, Image 

# # To get the dialog box to open when required  
# from tkinter import filedialog

#choosing the face
#this will be imported in a later version of the app
#we have to navigate to Sample faces first because there are more csvs than faces.
os.chdir(os.path.join(os.path.dirname(os.curdir), 'Sample faces'))
#imageName = random.choice(os.listdir(os.curdir))
#fileName = imageName[:-13]
imagePath= None
image = None
first40faces= None
client_ratio = np.array([])
datastore_ratios = np.array([])
#filePath = "csv_files/"+fileName+".csv.chip.csv"

#this class organizes all of the frames

class NoseApp:
    def __init__(self, master):
        self.master = master
        #master.geometry("300x200")
        master.title("Smart Nose Surgery")
        self.master.geometry('400x300+%d+%d' % (self.master.winfo_width(), self.master.winfo_height()))
        self.label = Label(master, text="Greetings!")
        self.label.pack()

        self.upload_button = Button(master, text="Upload Image", command = upload_image_button)
        self.upload_button.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        self.upload_button.pack()

        self.start_button = Button(master, text="Start Process",  command = lambda: LastWindow(master))
        self.start_button.place(relx = 0.5, rely = 0.5, anchor = CENTER)  
        self.start_button.pack()

# TO_DO
# METHOD NEED TO BE CLEANED
def upload_image_button():
    faceFeats = UploadClass.Upload_Picture.open_img()
    
    def start_process(faceFeats):
        
        client_ratio = ratio_compute.calculate_ratio(faceFeats)
        
        datastore_ratios = ratio_compute.calculate_ratios()
        
        first40faces = KNNalg.get_neighbors(datastore_ratios, client_ratio , 5)

    
        for i in range(len(first40faces)):
            print(first40faces[i])
            
    start_process(faceFeats)
    
class LastWindow(Toplevel): 
      
    def __init__(self, master = None):           
        super().__init__(master = master) 
        self.title("Results") 
        self.geometry('400x300+%d+%d' % (self.master.winfo_width(), self.master.winfo_height()))
        label = Label(self, text ="Here should be pictures") 
        label.pack()
        
    
        
    
root = Tk()
my_gui = NoseApp(root)
root.mainloop()