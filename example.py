from geocode.geocode import Geocode
import json

gc = Geocode()

gc.load()  # load pickles
mydata = ['Tel Aviv', 'Mangalore 🇮🇳']

for input_text in mydata:
  locations = gc.decode(input_text)
  print(json.dumps(locations, indent=4))
