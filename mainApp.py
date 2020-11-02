# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 00:55:16 2020

@author: Chris Graziano
"""

#!/usr/bin/env python3

import tkinter as tk
from tkinter import font as tkfont
from PIL import ImageTk, Image
import os
import csv
import FacialFeatureClass
import takingPicture
import KNNalg
import ratioCompute
import numpy as np
import pandas as pd

fileName = []
first40faces = []
faceFeats = []  
clientRatio = np.array([])
datastoreRatios = np.array([])
ratioDf = None

#this class initializes the frame and manages it
class Mainframe(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = LoginFrame(self)
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget() # deletes the current frame
        self.frame = frame(self)
        self.frame.pack() # make new frame
#this class makes a login frame for security
class LoginFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Enter password")
        master.geometry("300x200")
        self.status = tk.Label(self, fg='red')
        self.status.pack()
        lbl = tk.Label(self, text='Enter password')
        lbl.pack()
        self.pwd = tk.Entry(self, show="*")
        self.pwd.pack()
        self.pwd.focus()
        self.pwd.bind('<Return>', self.check)
        btn = tk.Button(self, text="Done", command=self.check)
        btn.pack()
        btn = tk.Button(self, text="Cancel", command=self.quit)
        btn.pack()
    #checks the password
    def check(self, event=None):
        if self.pwd.get() == 'password':
            self.master.change(StartFrame)
        else:
            self.status.config(text="wrong password")
        
#this class is just a simple start frame        
class StartFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Welcome to Nose Whatever the Name")
        master.geometry("300x200")
        label = tk.Label(self, text="Welcome to the M-LAR experience", font=tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic"))
        label.pack(side="top", fill="x", pady=10)
        picButton = tk.Button(self, text="Take picture", command=lambda: self.master.change(PicFrame))
        picButton.pack()

#this class displays the frame that shows the image
class PicFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Nose Whatever the Name")
        takePic = takingPicture.TakePicture() #invokes takingPicture
        while True:
            if takePic != None:
                pat = takePic.getPatientFace()
                break
        global faceFeats
        faceFeats = FacialFeatureClass.FacialFeatures.getCoords(pat)
        label = tk.Label(self, text="This is your face", font=tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic"))
        label.pack(side="top", fill="x", pady=10)
        im = Image.fromarray(pat)
        img = ImageTk.PhotoImage(image = im)
        imageLabel = tk.Label(self, image = img)
        imageLabel.image = img
        imageLabel.pack(fill = "x", expand = "yes")
        picButton = tk.Button(self, text="Get neighbors", command=lambda: self.master.change(KNNFrame))
        picButton.pack()
        
class KNNFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Nose Whatever the Name")
        global faceFeats
        global first40faces
        global ratioDf
        if len(faceFeats) == 0:
            print("You didn't uplaod picture")
        else:
            clientRatio = ratioCompute.calculate_ratio(faceFeats)
            self.ratioDf = pd.read_csv(os.path.join(os.path.dirname(os.curdir), 'golden_ratio.csv'))
            datastoreRatios = self.ratioDf[['Delta x','Delta y']].to_numpy()
            first40faces = KNNalg.get_neighbors(datastoreRatios, clientRatio , 30)
            self.showResults()
    def showResults(self):
        global fileName
        os.chdir(os.path.join(os.path.dirname(os.curdir), 'Sample faces'))
        columns = 10
        imageCount = 0
        #go through each element in "element" and find file name in sample faces
        for i in range(len(first40faces)):
            element = self.ratioDf[(self.ratioDf["Delta x"] == first40faces[i][0]) & (self.ratioDf["Delta y"] == first40faces[i][1])]
            element = element.drop(columns = ["Delta x" ,"Delta y" , "dy/dx"])
            element["File"] = element["File"].str.replace(".csv" , ".jpg")
            element = element["File"].to_string(index = False)
            filePath = os.getcwd()+ "\\" + element.strip()
            try:
                imageCount += 1
                r, c = divmod(imageCount - 1, columns)
                img = Image.open(r'%s' % filePath)
                img = img.resize((150, 150), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                panel = tk.Label(self, image=img)
                panel.image = img
                panel.grid(row=r, column = c)
                #panel.pack(side="left", expand=True, fill="both")
            except Exception as e:
                print(e)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        
#starts the program
if __name__=="__main__":
    app=Mainframe()
    app.mainloop()