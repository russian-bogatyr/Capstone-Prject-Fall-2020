# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:25:02 2020

@author: super
"""

import csv

with open('21_1_2_20170104020235605.csv.chip.csv') as csv_file:
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