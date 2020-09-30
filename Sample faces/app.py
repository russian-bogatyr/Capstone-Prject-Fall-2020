# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:31:36 2020

@author: super
"""
#!/usr/bin/python

import tkinter as tk
                                  
r = tk.Tk() 
r.title('Nose Goes') 
r.geometry("300x300")
r.configure(background='grey')
button = tk.Button(r, text='Exit', width=25, command=r.destroy) 
button.pack(side = "bottom") 

img = tk.PhotoImage(file="22_1_2_20170105183412088.jpg.chip.jpg")
r.create_image(200, 200, image=img)

r.mainloop()