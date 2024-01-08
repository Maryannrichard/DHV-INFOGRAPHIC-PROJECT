# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:26:25 2024

@author: A
"""

# importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# reading te data.
df = pd.read_excel('World_Development_Indicators(9).xlsx')

# drop unnecessary columns
df = df.drop(['Country Code', 'Series Code'],axis=1)

# renaming df dataframe years
yr_rename = yr_rename = {
    '1990 [YR1990]': 1990,
    '1995 [YR1995]': 1995,
    '2000 [YR2000]': 2000,
    '2005 [YR2005]': 2005,
    '2010 [YR2010]': 2010,
    '2015 [YR2015]': 2015,
    '2020 [YR2020]': 2020
   }

df = df.rename(yr_rename,axis=1)

# check for Nan values
df.isna().sum()

# Set the visual library style
sns.set(style="darkgrid")

# Set background color for the dashboard
fig = plt.figure(figsize=(15, 12), facecolor='black')

# Set the background color of the axes and figure
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['figure.facecolor'] = 'black'

# Set the text color to white
plt.rcParams['text.color'] = 'white'

# Set x and y axis label colors to white
plt.rcParams['axes.labelcolor'] = 'white'

# Set the color of the ticks label
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

# Set Title for the dashboard
plt.suptitle('SOME FACTORS THAT INFLUENCES POPULATION GROWTH', 
             fontsize=15, ha='center',fontweight='bold')
plt.figtext(0.5, 0.95, 'Ukonu Chizoba. ID no: 21089329', ha='center', 
            va='center', fontsize=12, color='red',fontweight='bold')