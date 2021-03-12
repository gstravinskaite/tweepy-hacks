import pandas as pd
import sentiment

radius = '100km'

df_loc = pd.read_csv('locations.csv')
topics = open('topics.txt')
topics = topics.read()
topics = topics.split("\n")

df_out = pd.DataFrame(columns=['Location','Lat','Long','Topic','Positive','Negative','Neutral'])

# for row in df_loc.rows:
for index, row in df_loc.iterrows():
    name = row['LOCATION']
    lat = row['LAT']
    lng = row['LONG']

    geocode = str(lat)+','+str(lng)+','+radius    
    for topic in topics:
      pos, neg, neutral = sentiment.main(query=topic, geocode=geocode, printing=False)
      print(name, topic, pos, neg, neutral)

      new_row = {'Location':name, 'Lat':lat, 'Long':lng, 'Topic': topic, 'Positive':pos, 'Negative':neg, 'Neutral':neutral}
      df_out = df_out.append(new_row, ignore_index=True)

df_out.to_csv('out.csv')
