# Local-geocode :earth_americas:

This is a very simple geocoding library which runs fully locally (without calling any APIs) and has therefore no limits in terms of processing. It runs very fast due to using an efficient in-memory datastructure called [Flashtext](https://github.com/vi3k6i5/flashtext). It uses data from http://www.geonames.org/.

# Usage

1) Clone this repo
```
git clone git@github.com:mar-muel/local-geocode.git && cd local-geocode
```
2) Install dependencies

Install dependencies with conda:
```
conda env create -f environment.yml
```
(Or using `pip install -r requirements.txt`)

3) Download data from geonames.org by running
```
source download_data.sh
```
Note that this will take approx 1.4GB of disk space!

4) Next we will create the data structures needed to efficiently decode locations from input text. This only needs to be run once!
```
python main.py prepare
```
The resulting 2 pickle files are about ~50MB in size and will be stored to your `/tmp` directory.

5) Now we should be all set! :raised_hands: We can test it via CLI:
```
python main.py decode -i "new delhi, new york, zurich"
```
Output:
```python
[
  {'name': 'New York', 'country_code': 'US', 'longitude': -75.4999, 'latitude': 43.00035},
  {'name': 'Zurich', 'country_code': 'CH', 'longitude': 8.66667, 'latitude': 47.41667},
  {'name': 'New Delhi', 'country_code': 'IN', 'longitude': 77.22539, 'latitude': 28.635679999999997}
]

```

# Usage in code
Using the CLI for decoding is slow since it has to load the pickles on every call. Use the script as follows:
```python
from geocode.geocode import Geocode

gc = Geocode()

gc.prepare() # compute pickles if not already present

gc.init()  # load pickles

mydata = ['Tel Aviv', 'busan', 'chattanooga']

for input_text in mydata:
  locations = gc.decode(input_text)
  print(locations)

# [{'name': 'Tel Aviv', 'country_code': 'IL', 'longitude': 34.79995, 'latitude': 32.084140000000005}]
# [{'name': 'Busan', 'country_code': 'KR', 'longitude': 129.05, 'latitude': 35.13333}]
# [{'name': 'Chattanooga', 'country_code': 'US', 'longitude': -85.30968, 'latitude': 35.045629999999996}]
```
The easiest way to integrate `local-geocode` to your project is to simply copy the folder `geocode` into your project root. After this you should be able to use the code as described above.

# Configuration
The `prepare()` function accepts two parameters
* `min_population_cutoff` (default: 30k): Cities below this population size are excluded
* `large_city_population_cutoff` (default: 200k): Cities with a population size larger than this will be prioritized. Example: "New York, USA" will result in "New York" as the first result, and not "USA".

Note that the prioritization is not always perfect.
