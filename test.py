from geocode.geocode import Geocode

gc = Geocode()

gc.prepare() # compute pickles if not already present
gc.init()  # load pickles
mydata = ['Tel Aviv', 'busan', 'chattanooga']

for input_text in mydata:
  locations = gc.decode(input_text)
  print(locations)
