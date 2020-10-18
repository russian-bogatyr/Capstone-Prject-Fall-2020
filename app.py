# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:29:09 2020

@author: Chris Graziano
"""
import tkinter as tk
from tkinter import font as tkfont
from PIL import ImageTk, Image
import csv
import random
import os
import FacialFeatureClass
import KNNalg
import taking_picture as pic


#choosing the face
#this will be imported in a later version of the app
#we have to navigate to Sample faces first because there are more csvs than faces.
os.chdir(os.path.join(os.path.dirname(os.curdir), 'Sample faces'))
imageName = random.choice(os.listdir(os.curdir))
fileName = imageName[:-13]
imagePath= imageName
filePath = "csv_files/"+fileName+".csv.chip.csv"
faceFeats = FacialFeatureClass.FacialFeatures(imagePath)

#this class organizes all of the frames
class NoseApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    #this method configures and displays a frame
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        self.title('Nose Goes')
        frame.configure(background='light blue')

#this class displays the initial frame
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the M-LAR experience", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        picButton = tk.Button(self, text="Take picture", command=lambda: runTakingPicture(controller))
        picButton.pack()

#this class displays the frame that shows the image

#This function will run the taking_picture file
def runTakingPicture(controller):
    runner = pic.TakingPicture()
    while True:
        if runner != None:
            controller.show_frame("PageOne")
            break
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is your selected face", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text=faceFeats.calculateFacialSize(), font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        img = ImageTk.PhotoImage(Image.open(pic.getPatientFace()))
        imageLabel = tk.Label(self, image = img)
        imageLabel.image = img
        imageLabel.pack(fill = "x", expand = "yes")
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Display the csv(s)", command=lambda: controller.show_frame("PageTwo"))
        button.pack()
        button2.pack()

#this class displays the frame that shows the file
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="These are the facial coordinates", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        textBox = tk.Text(self)
        os.chdir(os.pardir)
        with open(filePath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    textBox.insert(tk.INSERT, f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    textBox.insert(tk.INSERT, f'\t{row[0]} x:{row[1]}, y:{row[2]}')
                    line_count += 1
        textBox.pack(side = "top")
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = NoseApp()
    app.mainloop()
