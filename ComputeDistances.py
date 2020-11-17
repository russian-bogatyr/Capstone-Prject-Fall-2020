# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:02:55 2020

@author: super & Jacob Preseau
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

# Calculates the distances between normalized nose points
def calcDifference(userArray, targetArray):
  distances = []
  targetNose = normalizeNosePoints(targetArray)
  userNose = normalizeNosePoints(userArray)
  for n in range(0,8):
      distances.append(euclideanDistance(userNose[n], targetNose[n]))
  return distances

# Calculates the coordinate differences between nose points
def calcDifferencesArray(userArray, targetArray):
    differences = []
    targetNose = normalizeNosePoints(targetArray)
    userNose = normalizeNosePoints(userArray)

    return targetRatio - userRatio

# Normalizes and returns the entire face coordinate array.
def normalizePoints(facial_coordinates):
    # Use points 0 and 16 as the x interval, 24 and 8 as the y interval
    minX = facial_coordinates[0][0]
    maxX = facial_coordinates[16][0]
    minY = facial_coordinates[24][1]
    maxY = facial_coordinates[8][1]

    normalized_points = []

    for i in range(len(facial_coordinates)):
        newX = (facial_coordinates[i][0] - minX) / (maxX - minX)
        newY = (facial_coordinates[i][1] - minY) / (maxY - minY)

        normalized_points.append([newX, newY])

    return normalized_points

# Normalizes and returns just the nose points.
def normalizeNosePoints(facial_coordinates):
    # Use points 0 and 16 as the x interval, 24 and 8 as the y interval
    minX = facial_coordinates[0][0]
    maxX = facial_coordinates[16][0]
    minY = facial_coordinates[24][1]
    maxY = facial_coordinates[8][1]

    normalized_points = []

    for i in range(27, 35):
        newX = (facial_coordinates[i][0] - minX) / (maxX - minX)
        newY = (facial_coordinates[i][1] - minY) / (maxY - minY)

        normalized_points.append([newX, newY])

    return normalized_points
