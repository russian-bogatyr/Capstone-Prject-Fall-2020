# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:02:55 2020

@author: super
"""
import KNNalg
import ratioCompute
import os
import pandas as pd

def calcDifference(userArray, targetArray):
  clientRatio = ratioCompute.calculate_ratio(targetArray)
  ratioDf = pd.read_csv(os.path.join(os.path.dirname(os.curdir), 'golden_ratio.csv'))
  datastoreRatios = ratioDf[['Delta x','Delta y']].to_numpy()
  distances = KNNalg.euclidean_distance(datastoreRatios, clientRatio)
  return distances
  