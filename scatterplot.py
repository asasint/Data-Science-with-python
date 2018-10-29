import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv("population_csv.csv",skiprows=[0], names=['CountryName','CountryCode','Year','Value'])
dd=df.groupby("CountryName")
df1=dd.Year
df2=dd.Value
plt.scatter(df1,df2)
plt.show()
