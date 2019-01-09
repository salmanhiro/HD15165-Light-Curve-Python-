# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

df = pd.read_csv('hasil.csv', delim_whitespace=True)  
      #an empty list to store the second column
      
timeJD = df.iloc[:,0].values
VWAri = df.iloc[:,1].values
Check = df.iloc[:,2].values
Comparation = df.iloc[:,3].values

#This block for VW Ari
plt.figure(0)
plt.scatter(timeJD,VWAri, label = 'VW Ari')
plt.scatter(timeJD,Check, label = 'Check')
plt.scatter(timeJD,Comparation, label = 'Comparation')
plt.title ("Instrumental Magnitude Over Time")
plt.xlabel("Time in JD")
plt.ylabel("Instrumental Magnitude")
plt.legend(loc='upper left')

#For differential photometry
VWAriCh = VWAri - Check
VWAriCom = VWAri - Comparation
plt.figure(1)
plt.scatter(timeJD,VWAriCh, label = 'VW Ari - Comparation')
plt.scatter(timeJD,VWAriCom, label = 'VW Ari - Comparation')
plt.xlabel("Time in JD")
plt.ylabel("Delta Instrumental Magnitude")
plt.title ("Differential Photometry")
plt.legend(loc='lower left')





