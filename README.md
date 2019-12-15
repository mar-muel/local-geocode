# Local-geocode :earth_americas:

This is a very simple geocoding library which runs fully locally (without calling any APIs) and has therefore no limits in terms of processing. It runs very fast due to using an efficient in-memory datastructure called [Flashtext](https://github.com/vi3k6i5/flashtext). It uses data from http://www.geonames.org/.

# Usage

1) Clone this repo
```
git clone git@github.com:mar-muel/local-geocode.git && cd local-geocode
```
2) Install dependencies
You can either install dependencies by using conda:
```
conda env create -f environment.yml
```
(Or install them manually using `pip install pandas tqdm flashtext`)

3) Download data from geonames.org by running
```
source download_data.sh
```
Note that this will take approx 1.4GB of disk space!

4) Next we will create the data structures needed to efficiently decode locations from input text. This only needs to be run once!
```
python main.py prepare
```
If you want to include alternate names (such as L.A. for Los Angeles) make sure to add the `--with-altnames` flag:
```
python main.py prepare --with-altnames
```
The resulting pickle files are about ~50MB in size.

5) Now we should be all set! We can test it via CLI:
```
python main.py decode -i 'I live both in New York and in New Delhi.'
```
Output:
```
[{'name': 'New Delhi', 'country_code': 'IN', 'longitude': 77.22539, 'latitude': 28.635679999999997}, {'name': 'New York', 'country_code': 'US', 'longitude': -75.4999, 'latitude': 43.00035}]
```
Among other parameters, the output will be sorted by population size (see below).

# Usage in code
Using the CLI for decoding is slow since it has to load the pickles on every call. Use the script as follows:
```python
from geocode.geocode import Geocode

gc = Geocode(with_altnames=False)
gc.init()  # load pickles

mydata = ['I live both in new york and in New Delhi.', 'Zürich, Switzerland']

for input_text in mydata:
  locations = gc.decode(input_text)
  print(locations)
```

(See `test.py`)

# Sorting of output
In case multiple locations could be detected the output will be sorted by the following priorities:
* Places (such as cities) are prioritized over administrative areas (such as countries or provinces)
* Places: sorted by their importance w.r.t. to whether they are the seat of a administrative region, also see https://www.geonames.org/export/codes.html
* Admin areas: Sorted like so ADM2 > ADM1 > ADM3 > ADM4 (second order devisions are prioritized over countries, afterward priority decreases by admin level)
* Within each class prioritize by locations with higher population size

Note that the prioritization is not perfect. If accuracy is important to you, you may want to use an API-based library such as `geopy` (https://pypi.org/project/geopy/)
