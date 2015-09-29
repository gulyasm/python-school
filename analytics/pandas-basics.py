# Import the pandas module
# The as close might be omitted
import pandas as pd

df = pd.read_csv('http://perso.telecom-paristech.fr/~eagan/class/as2013/inf229/data/film.csv', sep=';', encoding="iso8859", skiprows=[1])

