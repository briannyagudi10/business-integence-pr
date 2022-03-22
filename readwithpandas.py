import numpy


import tkinter #library for graphics
import tkk,filedialog 
from tkinter import Y
from tkinter.tix import COLUMN
import pandas as pd
import matplotlib.pyplot as plt
tabl= pd.read_excel (r'D:\bI ass\population.xlsx') #read the file in its location

print(tabl)# prints the table

plt.plot(tabl["Year"], tabl["population(millions)"])  #plot the two points
plt.xlabel('Year')
plt.ylabel('population(millions)')
plt.title("KENYAN POPULATION GROWTH IN THE PAST TEN YEARS") #display tittle
plt.show() #display inform of line chart

#print(tabl)