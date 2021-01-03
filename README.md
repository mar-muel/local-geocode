# Local-geocode :earth_americas:

This is a very simple geocoding library which runs fully locally (without calling any APIs) and has therefore no limits in terms of processing. It runs very fast due to using an efficient in-memory datastructure called [Flashtext](https://github.com/vi3k6i5/flashtext). It uses data from http://www.geonames.org/.

This project is mainly used in the context of decoding data from the "user.location" field of tweets but it can in principle be used on any address/location raw text field. Note that if you need very precise geographical information it is better to use one of the many available APIs. By default this repo only detects places with more than 30k inhabitants.

I have compared the predictions by local-geocode with geopy for 500 Twitter user locations. Local-geocode performs signficantly better (85% accuracy) than geopy (64% accuracy). Read more about the benchmark [here](benchmark/benchmark.md).


# Example usage
Local-geocode is able to parse arbitrary location names in many languages, as well as numerous alternative names of places and returns geographic information.

```python
from geocode.geocode import Geocode

gc = Geocode()

gc.prepare() # compute pickles if not already present

gc.init()  # load pickles

mydata = ['Tel Aviv', 'Mangalore 🇮🇳']

for input_text in mydata:
    locations = gc.decode(input_text)
    print(locations)

[
    {
        "name": "Tel Aviv",
        "official_name": "Tel Aviv",
        "country_code": "IL",
        "longitude": 34.780570000000004,
        "latitude": 32.08088,
        "geoname_id": "293397",
        "location_type": "city",
        "population": 432892
    }
]

[
    {
        "name": "Mangalore",
        "official_name": "Mangalore",
        "country_code": "IN",
        "longitude": 74.85603,
        "latitude": 12.91723,
        "geoname_id": "1263780",
        "location_type": "city",
        "population": 417387
    },
    {
        "name": "\ud83c\uddee\ud83c\uddf3",
        "official_name": "Republic of India",
        "country_code": "IN",
        "longitude": 79.0,
        "latitude": 22.0,
        "geoname_id": "1269750",
        "location_type": "country",
        "population": 1352617328
    }
]

[
    {
        "name": "\ud83c\udde8\ud83c\udde6",
        "country_code": "CA",
        "longitude": -113.64258000000001,
        "latitude": 60.10867,
        "geoname_id": "6251999",
        "location_type": "country",
        "population": 37058856
    }
]
```

# Install

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
python main.py decode -i "new delhi, L.A., and zurich"
```
Output:
```json
[
    {"name": "New Delhi", "official_name": "New Delhi", "country_code": "IN", "longitude": 77.22445, "latitude": 28.635759999999998, "geoname_id": "1261481", "location_type": "city", "population": 317797},
    {"name": "Zurich", "official_name": "Kanton Z\u00fcrich", "country_code": "CH", "longitude": 8.66667, "latitude": 47.41667, "geoname_id": "2657895", "location_type": "admin1", "population": 1289559},
    {"name": "L.A.", "official_name": "Los Angeles", "country_code": "US", "longitude": -118.24368, "latitude": 34.05223, "geoname_id": "5368361", "location_type": "city", "population": 3971883}
]
```

# Usage
The easiest way to integrate `local-geocode` to your project is to simply copy the folder `geocode` into your project root. After this you should be able to use the code as described above.

## Parallelized
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

## Configuration
The `Geocode()` function accepts the following parameters:
* `min_population_cutoff` (default: 30k): Places below this population size are excluded
* `large_city_population_cutoff` (default: 200k): Cities with a population size larger than this will be prioritized. Example: "Los Angeles, USA" will result in "Los Angeles" as the first result, and not "USA".
* `location_types`: Provide a list of location types which you would like to filter. By default it uses all location types (i.e. `['city', 'place', 'country', 'admin1', 'admin2', 'admin3', 'admin4', 'admin5', 'admin6', 'admin_other', 'continent', 'region']`).

Local-geocode sorts the output by the following prioritization:
1. Large cities (`population size > large_city_population_cutoff`)
2. States/provinces
3. Countries
4. Places
5. Counties (admin levels larger than 1)
6. Continents
7. Regions

Please open an issue, if you run into problems!
