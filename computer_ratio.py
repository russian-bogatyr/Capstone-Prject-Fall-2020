import pandas as pd
import os

count=0
filepath = r"C:\Users\chint\OneDrive - Embry-Riddle Aeronautical University\Documents\senior_design\Machine-Learning-Nose-Jobs\csv_files"
for filename in os.listdir(filepath):
    count=count=1
    data = pd.read_csv(os.path.join(filepath,filename))
    #print(data.head(5))
    #if count==5:
    #    break
