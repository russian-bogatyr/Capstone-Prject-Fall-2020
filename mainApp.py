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
import ComputeDistances
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

pat = None
first40faces = []
faceFeats = []
clientRatio = np.array([])
datastoreRatios = np.array([])
ratioDf = None
clusterArray = []
Kval = 0
targetFace = "21_1_3_20170104231627770"

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
    def assignCluster(self, desArray):
        global clusterArray
        clusterArray = desArray
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
        global pat
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
        picButton = tk.Button(self, text="Start Process", command=lambda: [self.check, self.master.change(ClusterFrame)])
        picButton.pack()

        # Temporary button, until cluster frame works
        changesButton = tk.Button(self, text="Display Changes", command=lambda: self.master.change(ChangesFrame))
        changesButton.pack()

    def check(self, event=None):
        global Kval
        if self.pwd.get().isdigit():
            Kval = int(self.pwd.get())
            print("This is kval form other call "+ str(Kval))
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
        global Kval
        clusterOneArray = []
        clusterTwoArray = []
        clusterThreeArray = []
        clusterFourArray = []
        clusterFiveArray = []
        if len(faceFeats) == 0:
            print("You didn't uplaod picture")
        else:
            filename = "dist.csv"
            print("Hello world")
            clientRatio = ratioCompute.calculate_ratio(faceFeats)
            print("hello universe")
            self.ratioDf = pd.read_csv(os.path.join(os.path.dirname(os.curdir), 'golden_ratio.csv'))
            datastoreRatios = self.ratioDf[['Delta x','Delta y']].to_numpy()
            print("hello galaxy")
            first40faces = KNNalg.get_neighbors(datastoreRatios, clientRatio , Kval)
            print(Kval)
            for i in range(Kval):
                print("I am inside for loop")
                element = self.ratioDf[(self.ratioDf["Delta x"] == first40faces[i][0]) & (self.ratioDf["Delta y"] == first40faces[i][1])]
                element = element.drop(columns = ["Delta x" ,"Delta y" , "dy/dx"])
                element["File"] = element["File"].str.replace(".csv" , ".jpg")
                element = element["File"].to_string(index = False)
                filePath = os.getcwd()+ "\\dataset_3\\" + element.strip()
                print(filePath)
                with open(filename) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    for row in csv_reader:
                        print(row)
                        if line_count == 0:
                            line_count += 1
                        else:
                            print(filePath)
                            print(row[0])
                            if filePath.split(os.path.sep)[-1] == row[0]:
                                if row[1] == "Very broad nose":
                                    print('VBN')
                                    clusterOneArray.append(row[0])
                                if row[1] == "Broad nose":
                                    print('BN')
                                    clusterTwoArray.append(row[0])
                                if row[1] == "Medium nose":
                                    print('MN')
                                    clusterThreeArray.append(row[0])
                                if row[1] == "Narrow nose":
                                    print('NN')
                                    clusterFourArray.append(row[0])
                                if row[1] == "Very Narrow nose":
                                    print('VNN')
                                    clusterFiveArray.append(row[0])
                            line_count += 1
        self.showResults(clusterOneArray, clusterTwoArray, clusterThreeArray, clusterFourArray, clusterFiveArray)
    def showResults(self,clusterOneArray, clusterTwoArray, clusterThreeArray, clusterFourArray, clusterFiveArray):
        os.chdir(os.path.join(os.path.dirname(os.curdir), 'dataset_3'))
        r=0
        c=0
        if clusterOneArray:
            filePath = clusterOneArray[0]
            img = Image.open(r'%s' % filePath)
            img = img.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.grid(row=r, column = c)
            chooseButton = tk.Button(self, text="Start Process", command=lambda: [self.master.assignCluster(clusterOneArray), self.master.change(FinalFrame)])
            chooseButton.grid(row=r+1, column = c)
            c += 1
        if clusterTwoArray:
            filePath = clusterTwoArray[0]
            img = Image.open(r'%s' % filePath)
            img = img.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.grid(row=r, column = c)
            chooseButton = tk.Button(self, text="Start Process", command=lambda: [self.master.assignCluster(clusterTwoArray), self.master.change(FinalFrame)])
            chooseButton.grid(row=r+1, column = c)
            c += 1
        if clusterThreeArray:
            filePath = clusterThreeArray[0]
            img = Image.open(r'%s' % filePath)
            img = img.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.grid(row=r, column = c)
            print(clusterThreeArray)
            chooseButton = tk.Button(self, text="Start Process", command=lambda: [self.master.assignCluster(clusterThreeArray), self.master.change(FinalFrame)])
            chooseButton.grid(row=r+1, column = c)
            c += 1
        if clusterFourArray:
            filePath = clusterFourArray[0]
            img = Image.open(r'%s' % filePath)
            img = img.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.grid(row=r, column = c)
            chooseButton = tk.Button(self, text="Start Process", command=lambda: [self.master.assignCluster(clusterFourArray), self.master.change(FinalFrame)])
            chooseButton.grid(row=r+1, column = c)
            c += 1
        if clusterFiveArray:
            filePath = clusterFiveArray[0]
            img = Image.open(r'%s' % filePath)
            img = img.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.grid(row=r, column = c)
            chooseButton = tk.Button(self, text="Start Process", command=lambda: [self.master.assignCluster(clusterFiveArray), self.master.change(FinalFrame)])
            chooseButton.grid(row=r+1, column = c)
            c += 1
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

class FinalFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Here is your desired cluster")
        master.geometry("500x500")
        r=0
        c=0
        for i in range(len(clusterArray)):
            filePath = clusterArray[i]
            img = Image.open(r'%s' % filePath)
            img = img.resize((150, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(self, image=img)
            panel.image = img
            panel.grid(row=r, column = c)
            r=r+1
class ChangesFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Welcome to Smart Nose Surgery")
        master.geometry("500x500")

        global pat
        global faceFeats
        global targetFace

        label = tk.Label(self, text="This is the difference in nose points", font=tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic"))
        label.pack(side="top", fill="x", pady=10)

        # Create the image
        user_image = Image.fromarray(pat)

        # Create the sets of points
        user_points = faceFeats
        target_points = pd.read_csv("csv_files/" + targetFace + ".csv.chip.csv")[["x", "y"]].values

        # Normalize the target points
        normalized_points = ComputeDistances.normalizePoints(target_points)

        # Unnormalize the target points with respect to the user's face
        unnormalized_points = ComputeDistances.unNormalizePoints(normalized_points, user_points[0][0], user_points[16][0], user_points[24][1], user_points[8][1], user_points[30])

        # Create the figure
        width, height = user_image.size
        fig = Figure(figsize = (width / 100, height / 100), dpi = 100)

        # Make the plot and put the nose points on top
        image_plot = fig.add_subplot(111)
        image_plot.imshow(pat)
        image_plot.plot([x[0] for x in unnormalized_points[27:36]], [y[1] for y in unnormalized_points[27:36]], "r*")
        image_plot.set_axis_off()

        # Create the canvas
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack()



#starts the program
if __name__=="__main__":
    app=Mainframe()
    app.mainloop()
