from geocode.geocode import Geocode

gc = Geocode(with_altnames=False)
gc.init()  # load pickles

mydata = ['I live both in new york and in New Delhi.', 'Zürich, Switzerland']

for input_text in mydata:
  locations = gc.decode(input_text)
  print(locations)
