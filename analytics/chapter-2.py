###############################
# Chapter 2: Read, Write data
###############################

# Import the pandas module
# The as close might be omitted
import pandas as pd

## Note that tab completion works.
# Dataframe
# Read a real dataset
df = pd.read_csv('data/e0.csv', sep=',', encoding="utf-8")

## Here we show the other read methods via TAB completion
df.to_pickle('data/e0.pickle')
df.to_json('data/e0.json')
## to_sql can write directly to DB


