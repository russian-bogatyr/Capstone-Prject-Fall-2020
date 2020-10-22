import ratio_compute
import pandas as pd
data = ratio_compute.calculate_ratios()
empty_arr = data[['Delta x','Delta y']].to_numpy()
print(empty_arr)

