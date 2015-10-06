###################################
# Chapter 3: Advanced operations
###################################

# Import the pandas module
# The as close might be omitted
import pandas as pd

## Note that tab completion works.
# Dataframe
# Read a real dataset
df = pd.read_csv('data/e0.csv', sep=',', encoding="utf-8")
# Selecting multiple columns
df = df[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']]
# Renaming columns
df.columns = ['HT', 'AT','HG','AG']

# Returns a new DataFrame
df.rename(columns={'HT': 'HomeTeam'})
df.column
# With inplace the columns are changed on the original
df.rename(columns={'HT': 'HomeTeam'}, inplace=True)
df.column

