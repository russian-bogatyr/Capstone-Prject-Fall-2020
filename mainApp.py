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
import TakingPicture
import KNNalg
import ratioCompute
import numpy as np
import pandas as pd

first40faces = []
faceFeats = []  
clientRatio = np.array([])
datastoreRatios = np.array([])
ratioDf = None
clusterArray = []
Kval = 0

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
        master.geometry("500x500")
        self.status = tk.Label(self, fg='red')
        lbl = tk.Label(self, text='Enter password')
        lbl.grid(row=1, column = 1, sticky = "NS")
        self.pwd = tk.Entry(self, show="*")
        self.pwd.grid(row=1, column = 2)
        self.pwd.focus()
        self.pwd.bind('<Return>', self.check)
        enterBtn = tk.Button(self, text="Done", command=self.check)
        enterBtn.grid(row=2, column = 2, sticky="ew")
        closeBtn = tk.Button(self, text="Cancel", command=self.quit)
        closeBtn.grid(row=2, column = 1, sticky="ew")
        master.grid_rowconfigure((0,3), weight=1)
        master.grid_columnconfigure((0,3), weight=1)
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
        master.title("Welcome to Smart Nose Surgery")
        master.geometry("500x500")
        label = tk.Label(self, text="Welcome to Smart Nose Surgery", font=tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic"))
        label.pack(side="top", fill="x", pady=10)
        picButton = tk.Button(self, text="Take picture", command=lambda: self.master.change(PicFrame))
        picButton.pack()

#this class displays the frame that shows the image
class PicFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Welcome to Smart Nose Surgery")
        master.geometry("500x500")
        takePic = TakingPicture.TakePicture() #invokes takingPicture
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
        imageLabel.pack(fill = "x")
        self.status = tk.Label(self, fg='red')
        self.pwd = tk.Entry(self, show="*")
        self.pwd.pack()
        self.pwd.focus()
        self.pwd.bind('<Return>', self.check)
        picButton = tk.Button(self, text="Start Process", command=lambda: self.master.change(ClusterFrame))
        picButton.pack()
        
    def check(self, event=None):
        global Kval
        if self.pwd.get().isdigit():
            Kval = int(self.pwd.get())
            self.master.change(ClusterFrame)
        else:
            self.status.config(text="please enter an integer value")
class ClusterFrame(tk.Frame): 
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Nose Whatever the Name")
        global faceFeats
        global first40faces
        global ratioDf
        clusterOneArray = []
        clusterTwoArray = []
        clusterThreeArray = []
        clusterFourArray = []
        clusterFiveArray = []
        if len(faceFeats) == 0:
            print("You didn't uplaod picture")
        else:
            filename = "dist.csv"
            clientRatio = ratioCompute.calculate_ratio(faceFeats)
            self.ratioDf = pd.read_csv(os.path.join(os.path.dirname(os.curdir), 'golden_ratio.csv'))
            datastoreRatios = self.ratioDf[['Delta x','Delta y']].to_numpy()
            first40faces = KNNalg.get_neighbors(datastoreRatios, clientRatio , Kval)
            for i in range(len(first40faces)):
                with open(filename) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0:
                            line_count += 1                        
                        else:                    
                            if row[1] == "Overly broad nose":
                                print('OBN')
                                clusterOneArray.append(row[0])
                            if row[1] == "Very broad nose":
                                print('VBN')
                                clusterTwoArray.append(row[0])
                            if row[1] == "Broad nose":
                                print('BN')
                                clusterThreeArray.append(row[0])
                            if row[1] == "Medium nose":
                                print('MN')
                                clusterFourArray.append(row[0])
                            if row[1] == "Narrow nose":
                                print('NN')
                                clusterFiveArray.append(row[0])
                            line_count += 1
        self.showResults(clusterOneArray, clusterTwoArray, clusterThreeArray, clusterFourArray, clusterFiveArray)
    def showResults(self,clusterOneArray, clusterTwoArray, clusterThreeArray, clusterFourArray, clusterFiveArray):
        os.chdir(os.path.join(os.path.dirname(os.curdir), 'Sample faces'))
        r=0
        c=0
        #go through each element in "element" and find file name in sample faces
        if clusterOneArray:
            filePath = clusterOneArray[1]
            img = Image.open(r'%s' % filePath)
            img = img.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.grid(row=r, column = c)
            r += 1
            c += 1
        if clusterTwoArray:
            filePath = clusterTwoArray[1]
            img = Image.open(r'%s' % filePath)
            img = img.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.grid(row=r, column = c)
            r += 1
            c += 1
        if clusterThreeArray:
            filePath = clusterThreeArray[1]
            img = Image.open(r'%s' % filePath)
            img = img.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.grid(row=r, column = c)
            r += 1
            c += 1
        if clusterFourArray:
            filePath = clusterFourArray[1]
            img = Image.open(r'%s' % filePath)
            img = img.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.grid(row=r, column = c)
            r += 1
            c += 1
        if clusterFiveArray:
            filePath = clusterFiveArray[1]
            img = Image.open(r'%s' % filePath)
            img = img.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.grid(row=r, column = c)
            r += 1
            c += 1
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        
#starts the program
if __name__=="__main__":
    app=Mainframe()
    app.mainloop()