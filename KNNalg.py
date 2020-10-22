# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 00:55:16 2020

@author: Chris Graziano
"""

#!/usr/bin/env python3

import numpy as np

def euclidean_distance(test_point, neighbor_point):
    return np.sqrt(np.sum((test_point - neighbor_point)**2))


def get_neighbors(data_set, test_point, num_neighbors):
   distances = []
   for set_row in data_set:
        dist = euclidean_distance(test_point, set_row)
        distances.append((set_row, dist))
   distances.sort(key=lambda tup: tup[1])
   neighbors = []
   for i in range(num_neighbors):
       neighbors.append(distances[i][0])
   return neighbors 

