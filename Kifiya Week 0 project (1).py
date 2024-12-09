#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df_benin = pd.read_csv(r'C:\Users\Rahel\Desktop\kifiya\data\data\benin-malanville.csv')
df_sierra_leone = pd.read_csv(r'C:\Users\Rahel\Desktop\kifiya\data\data\sierraleone-bumbuna.csv')
df_togo = pd.read_csv(r'C:\Users\Rahel\Desktop\kifiya\data\data\togo-dapaong_qc.csv')

df_benin['Country'] = 'Benin'
df_sierra_leone['Country'] = 'Sierra Leone'
df_togo['Country'] = 'Togo'

df = pd.concat([df_benin, df_sierra_leone, df_togo], ignore_index=True)

print(df.head())


# In[4]:



# Print the first few rows of the dataset
print(df_benin.head())

# Check for data types and missing values
print(df_benin.info())


# In[5]:


import numpy as np

# List of columns that should not have negative or zero values
irradiance_columns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB']
temperature_columns = ['Tamb', 'TModA', 'TModB']
wind_columns = ['WS', 'WSgust']

# Replace invalid values (negative or zero) with NaN for appropriate columns
df_benin[irradiance_columns] = df_benin[irradiance_columns].apply(lambda x: np.where(x <= 0, np.nan, x))
df_benin[temperature_columns] = df_benin[temperature_columns].apply(lambda x: np.where(x < -50, np.nan, x))  # Extreme temperature values
df_benin[wind_columns] = df_benin[wind_columns].apply(lambda x: np.where(x < 0, np.nan, x))  # Negative wind speed doesn't make sense

# Check if the invalid values were replaced
print(df_benin.head())

