
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

note=pd.read_csv("PopulationData.csv")
df=note.groupby("LOCATION")["Value"].mean()

plt.plot(df,)
plt.xlabel("COUNTRY")
plt.ylabel("POPULATION")
plt.show()

"""
dd=note.groupby("TIME")["Value"].mean()
plt.title("Histogram")
plt.hist(dd,bins=5)
plt.show()
"""
"""ds=note.groupby("SUBJECT"="TOT")["Value"].mean()

a=np.array(note["TIME"])
bool=(a==2013)
plt.plot(bool)"""