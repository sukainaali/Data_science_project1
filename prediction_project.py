import pandas as pd
ship= pd.read_csv('cruise_ship_info.csv')
ship_columns= ship.head()
print(ship_columns)
ship_stat= ship.describe()
print(ship_stat)
