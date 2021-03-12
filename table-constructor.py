import pandas as pd
import sentiment

coordinates = pd.read_excel("lat_long.xls", index_col=0, header=0)
cords = coordinates.values.tolist()
for cord in cords:
  pos, neg, neutral = sentiment.main(query="Trump", geocode="{},{},100km".format(cord[0],cord[1]), printing=False)
  print(pos, neg, neutral)


#	print("Negative tweets percentage: {} %".format(percent_negative)) 
