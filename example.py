from geocode.geocode import Geocode
import json

gc = Geocode()

gc.prepare(recompute=False) # compute pickles if not already present
gc.init()  # load pickles
mydata = ['Tel Aviv', 'Mangalore 🇮🇳']

for input_text in mydata:
  locations = gc.decode(input_text)
  print(json.dumps(locations, indent=4))
