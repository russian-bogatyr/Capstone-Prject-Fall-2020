# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:29:09 2020

@author: Chris Graziano
"""

from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

class KnnAlgorithm:
    def euclidean_distance(test_point, neighbor_point):
        distance = 0.0
        for i in range(len(test_point)-1):
           distance += (test_point[i] - neighbor_point[i])**2
        return sqrt(distance)
    def get_neighbors(data_set, test_point, num_neighbors):
       distances = list()
       for set_row in data_set:
            dist = euclidean_distance(test_point, set_row)
            distances.append((set_row, dist))
       distances.sort(key=lambda tup: tup[1])
       neighbors = list()
       for i in range(num_neighbors):
           neighbors.append(distances[i][0])
       return neighbors
