# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:15:07 2020

@author: Anton
"""
import FacialFeatureClass
import numpy as np
# loading Python Imaging Library 
from PIL import ImageTk, Image 
  
# To get the dialog box to open when required  
from tkinter import filedialog

class Upload_Picture:
    
    # def openfn():
    #     filename = filedialog.askopenfilename(title='open')
    #     return filename
    def open_img():
        imagePath = filedialog.askopenfilename(title='open')
        img = Image.open(imagePath)
        img = img.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        # panel = Label(root, image=img)
        # panel.image = img
        # panel.pack()
        face_Feats = FacialFeatureClass.FacialFeatures.getCords(imagePath)

        return face_Feats