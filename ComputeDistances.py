# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:02:55 2020

@author: super
"""
import numpy as np

#nose points are 27-35
def calcNoseRatio(facial_coordinates):
    empty_ar = np.array([])
    for i in range(27, 35):
        x = facial_coordinates[i][0]
        y = facial_coordinates[i][1]
        noseArray = np.reshape(empty_ar, (-1, 2))
        noseArray = np.append(empty_ar, (x, y), axis = 0)
    return (noseArray)

def euclideanDistance(test_point, neighbor_point):
    # distance = 0.0
    # for i in range(len(test_point)-1):
    #     # dst = np.linalg.norm(test_point[i][1] - neighbor_point[i][1]) 
    #     distance += (test_point[i, 0:2] - neighbor_point[i, 0:2])**2
    return np.sqrt(np.sum((test_point - neighbor_point)**2))
    
def calcDifference(userArray, targetArray):
  targetRatio = calcNoseRatio(targetArray)
  userRatio = calcNoseRatio(userArray)
  for n in range(0,8):
      distances = euclideanDistance(userRatio[n], targetRatio[n])
  return distances
  