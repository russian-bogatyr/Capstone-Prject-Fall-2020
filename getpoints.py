import os
import pandas as pd
def getpoints(filename):
    data_194 = pd.read_csv(os.path.join(r".\DATASET_3_POINTS",filename+"_194.csv"))
    return data_194.loc[[135,138,148,151]]

