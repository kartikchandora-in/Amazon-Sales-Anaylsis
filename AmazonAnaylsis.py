import numpy as np
import pandas as pd

#Load the Data.
print("Load the Data.\n")

df = pd.read_csv("amazon.csv")

print(df.head())

print(df.shape)

print(df.columns)

print(df.info())