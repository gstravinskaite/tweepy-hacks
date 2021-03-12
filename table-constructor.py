import pandas as pd
import sentiment

radius = '100km'

df_loc = pd.read_csv('locations.csv')

# for row in df_loc.rows:
for index, row in df_loc.iterrows():
    name = row['LOCATION']
    lat = row['LAT']
    lng = row['LONG']

    geocode = str(lat)+','+str(lng)+','+radius    

    pos, neg, neutral = sentiment.main(query="Trump", geocode=geocode, printing=False)
    print(pos, neg, neutral)