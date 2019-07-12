#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 03:45:48 2019

@author: michelewaters
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:18:17 2019

@author: michelewaters
"""
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np
#Create dataframe with Year, Field, Ethnicity, and Percentage of Earned Doctorate information
df_gp = pd.read_csv('EarnedDoctorates_Race_10yrs_Transpose.csv', usecols = ['Year', 'Field', 'Ethnicity', 'Percentage'])   
#Create list of departments/fields
Dept=list(set(list(df_gp.Field)))
#Run for loop to create multiple dataframes, with each individual department
for department in Dept:
    df_Dept=df_gp.loc[df_gp['Field']==department]
#Plot using seaborn
    g=sns.catplot(data=df_Dept, x='Year', y='Percentage', hue="Ethnicity", palette="hls", kind="point")   
    plt.subplots_adjust(top=0.8)
    plt.title("Field: "+department, loc='center', fontsize=14)
    plt.show()

