# Local-geocode :earth_americas:

This is a very simple geocoding library which runs fully locally (without calling any APIs) and has therefore no limits in terms of processing. It runs very fast due to using an efficient in-memory datastructure called [Flashtext](https://github.com/vi3k6i5/flashtext). It uses data from http://www.geonames.org/.

This project is mainly used in the context of decoding data from the "user.location" field of tweets but it can in principle be used on any address/location raw text field. Note that if you need very precise geographical information it is better to use one of the many available APIs. By default this repo only detects places with more than 30k inhabitants.

# Usage

1) Clone this repo
```bash
git clone https://github.com/mar-muel/local-geocode.git && cd local-geocode
```
2) Install dependencies

Install dependencies with conda:
```bash
conda env create -f environment.yml
```
(Or using `pip install -r requirements.txt`)

3) Next we will download data from geonames.org and create the data structures needed to efficiently decode locations from input text. This only needs to be run once!
```bash
python main.py prepare
```
The resulting 2 pickle files are about ~50MB in size and will be stored under `/tmp/geocode_local`.

4) Now we should be all set! :raised_hands: We can test it via CLI:
```bash
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

# Usage in Python code
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

# Parallelized
If you have a large number of texts to decode, it might make sense to use `decode_parallel` which runs decode in parallel:
```python
gc = Geocode()

gc.prepare() # compute pickles if not already present

gc.init()  # load pickles

# a large number of items
mydata = ['Tel Aviv', ..,]
num_cpus = None # By default use all CPUs

locations = gc.decode_parallel(mydata, num_cpus=num_cpus)
print(locations)
```


# Configuration
The `prepare()` function accepts two parameters
* `min_population_cutoff` (default: 30k): Places below this population size are excluded
* `large_city_population_cutoff` (default: 200k): Cities with a population size larger than this will be prioritized. Example: "Los Angeles, USA" will result in "Los Angeles" as the first result, and not "USA".

If you change these values, make sure to add the recompute flag `python main.py prepare --recompute` or `gc.prepare(recompute=True)`.

Note that the prioritization is not always perfect. In general the prioritization is as follows:
1) Large cities
2) Administrative areas
3) Smaller places

Please open an issue, if you run into problems!
