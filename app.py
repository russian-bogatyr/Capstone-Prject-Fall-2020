# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:31:36 2020

@author: super
"""
#!/usr/bin/python

import tkinter as tk
import csv
import random
import os

r = tk.Tk()
textBox = tk.Text(r)
os.chdir(os.path.join(os.path.dirname(os.curdir), 'csv_files'))
with open(random.choice(os.listdir(os.curdir))) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            textBox.insert(tk.INSERT, f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            textBox.insert(tk.INSERT, f'\t{row[0]} x:{row[1]}, y:{row[2]}')
            line_count += 1
    textBox.insert(tk.INSERT, f'Processed {line_count} lines.')
    

textBox.pack()
r.title('Nose Goes') 
r.geometry("300x300")
r.configure(background='grey')
button = tk.Button(r, text='Exit', width=25, command=r.destroy) 
button.pack(side = "bottom") 

r.mainloop()