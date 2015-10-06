###############################
# Chapter 1: Basic operations
###############################

# Import the pandas module
# The as close might be omitted
import pandas as pd
import numpy as np

# Series
s = pd.Series([1,3,5,np.nan,6,8])
s.sum()
s.count()
# Filling the missing the values. Same as Dataframe later.
# np.nan is used to represent missing values
print(np.nan)
s.fillna(0)

# Note that tab completion works.
# Dataframe
# Read a real dataset
df = pd.read_csv('data/e0.csv', sep=',', encoding="utf-8")

# Dataframe is series with the same index.
type(df)
type(df.HomeTeam)
# To see the columns
df.columns
# To see the rows and columns
df.shape
# To see types
df.dtypes

## Statistical description
# Individual statistics
df.mean()
# To do it over the other axis (axis=1)
# What is an axis? How can an aggregation be appied?
df.mean(axis=1)
# Only the columns are shown that the aggregation can be applied on
df.max()

# To show detailed information
df.describe()

# Selecting columns
df['HomeTeam']
df[0:4].head(1)
df.columns[0:4]
df[df.columns[0:4]].head(1)

# Select rows based on values
# This is called boolean indexing
df.HomeTeam == 'Man United'
df[df.HomeTeam == 'Man United']

# To copy a dataframe
df_copy = df.copy()
df.shape

