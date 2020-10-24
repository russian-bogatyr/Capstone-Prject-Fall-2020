# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 00:55:16 2020

@author: Chris Graziano
"""

#!/usr/bin/env python3

import tkinter as tk
from tkinter import font as tkfont
from PIL import ImageTk, Image
import csv
import FacialFeatureClass
import takingPicture
import KNNalg
import ratioCompute

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
    
    def changePat(self, frame, pat):
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
        faceFeats = FacialFeatureClass.FacialFeatures(pat)
        label = tk.Label(self, text="This is your selected face", font=tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic"))
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text=faceFeats.calculateFacialSize(), font=tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic"))
        label.pack(side="top", fill="x", pady=10)
        im = Image.fromarray(pat)
        img = ImageTk.PhotoImage(image = im)
        imageLabel = tk.Label(self, image = img)
        imageLabel.image = img
        imageLabel.pack(fill = "x", expand = "yes")
        picButton = tk.Button(self, text="Get neighbors", command=lambda: [self.master.change(KNNFrame),KNNFrame.start_process(faceFeats)])
        picButton.pack()
        
class KNNFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Nose Whatever the Name")
    def start_process(faceFeats):
        clientRatio = ratioCompute.calculate_ratio(faceFeats)
        datastoreRatios = ratioCompute.calculate_ratios()
        first40faces = KNNalg.get_neighbors(datastoreRatios, clientRatio , 5)
        for i in range(len(first40faces)):
            print(first40faces[i])
            
#starts the program
if __name__=="__main__":
    app=Mainframe()
    app.mainloop()