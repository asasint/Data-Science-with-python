import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("population_csv.csv",skiprows=[0],names=["CountryName","CountryCode","Year","Value"])

df1=df[df.CountryName=="India"]
df2=df[df.CountryName=="Zimbabwe"]
df3=df[df.CountryName=="Mexico"]
df4=df[df.CountryName=="Uzbekistan"]
df5=df[df.CountryName=="United States"]

plt.plot(df1.Year,df1.Value,label="India")
plt.plot(df2.Year,df2.Value,label="Zimbabwe")
plt.plot(df3.Year,df3.Value,label="Mexico")
plt.plot(df4.Year,df4.Value,label="Uzbekistan")
plt.plot(df5.Year,df5.Value,label="United States")

plt.legend(loc="upper right")
plt.show()











