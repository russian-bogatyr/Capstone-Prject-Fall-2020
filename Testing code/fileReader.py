# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:25:02 2020

@author: super
"""

import csv
import os
import random

os.chdir(os.pardir)
os.chdir(os.path.join(os.path.dirname(os.curdir), 'csv_files'))
filename = random.choice(os.listdir(os.curdir))

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} x:{row[1]}, y:{row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines.')