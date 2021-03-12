import pandas as pd
import sentiment

locations = pd.read_csv('locations.csv')

pos, neg, neutral = sentiment.main(query="Trump", geocode="51.509865,-0.118092,100km", printing=False)
print(pos, neg, neutral)