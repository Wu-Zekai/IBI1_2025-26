import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_path = "/Users/wuzekai123/IBI1_2025-26/Practical10" 
os.chdir(data_path)

print("The current working directory is:", os.getcwd())

print("\nFiles in this directory:")
files = os.listdir()
print(files)

#check if the file is in the directory
if "dalys-rate-from-all-causes.csv" in files:
    print("\n✅ Successfully found the data file!")
else:
    print("\n File not found. Please check if the path is correct or if the filename is spelled correctly.")

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print("\nData preview (first 5 rows):")
print(dalys_data.head())