# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:29:09 2020

@author: Chris Graziano and Tony
"""
import numpy as np


def euclidean_distance(test_point, neighbor_point):
    # distance = 0.0
    # for i in range(len(test_point)-1):
    #     # dst = np.linalg.norm(test_point[i][1] - neighbor_point[i][1]) 
    #     distance += (test_point[i, 0:2] - neighbor_point[i, 0:2])**2
    return np.sqrt(np.sum((test_point - neighbor_point)**2))
    # return distance.euclidean(test_point, neighbor_point )


def get_neighbors(data_set, test_point, num_neighbors):
   distances = []
   for set_row in data_set:
        dist = euclidean_distance(test_point, set_row)
        distances.append((set_row, dist))
   distances.sort(key=lambda tup: tup[1])
   # distances.sort(key=operator.itemgetter(1))
   neighbors = []
   for i in range(num_neighbors):
       neighbors.append(distances[i][0])
   return neighbors 

