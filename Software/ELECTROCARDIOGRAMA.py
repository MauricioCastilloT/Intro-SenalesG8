
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

url = "https://raw.githubusercontent.com/nicoavilan/Bases-de-datos/main/ECG.csv"
df = pd.read_csv(url)
df


df = df.drop(labels=0, axis = 0)
df.head()

df.columns = ['Elapsed_time', 'I', 'II', 'III', 'AVR', 'AVL', 'AVF','V1', 'V2', 'V3', 'V4', 'V5', 'V6']
df.head()


print(df.loc[1,"II"])
type(df.loc[1,"II"])



df["II"] = pd.to_numeric(df["II"], downcast="float", errors='coerce')

print(df.loc[1,"II"])
type(df.loc[1,"II"])


print(df.loc[1,"Elapsed_time"])
type(df.loc[1,"Elapsed_time"])


df["Elapsed_time"] = df["Elapsed_time"].str.replace("'","", regex = False)
df.head()




print(df.loc[1,"Elapsed_time"])
type(df.loc[1,"Elapsed_time"])


df["Elapsed_time"] = pd.to_datetime(df["Elapsed_time"], format = "%M:%S.%f")
df.head()



df.loc[df["II"].idxmax(),"Elapsed_time"]

df["II"].idxmax()

df.loc[df["II"].idxmax(),"Elapsed_time"]

df.loc[df["II"].idxmax(),"Elapsed_time"]

df["II"].max()

(df.loc[df["II"].idxmax(),"Elapsed_time"].time(), df["II"].max())

df.loc[df["II"].idxmax(),"Elapsed_time"], df["II"].max()

plt.figure(figsize = (13,4))
plt.plot(df["Elapsed_time"],df["II"])
plt.plot(df.loc[df["II"].idxmax(),"Elapsed_time"], df["II"].max(), "ro", label= "Valor máximo")
plt.plot(df.loc[df["II"].idxmin(),"Elapsed_time"], df["II"].min(), "go", label= "Valor máximo")
plt.xlabel("Tiempo", size= 15)
plt.legend(loc = 1)
plt.show()
     

import matplotlib.animation as animation
from IPython.display import HTML

x = df["Elapsed_time"].values
y = df["II"].values
N = len(df)


fig=plt.figure(figsize= (12,4))
ax=fig.gca()

def actualizar(i):
  ax.clear()

  ax.plot(x[:i], y[:i],'-')
  ax.set_title("Electrocardiograma", fontweight="bold", size = 20)
  ax.set_xlabel("Tiempo", fontweight="bold", size = 15)
  ax.plot(x[i],  y[i],'o',markersize=10,color='r')
     


ani=animation.FuncAnimation(fig, actualizar, range(0,N,10), interval=30)
HTML(ani.to_html5_video())
    