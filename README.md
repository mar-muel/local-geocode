# Local-geocode :earth_americas:

This is a very simple geocoding library which runs fully locally (without calling any APIs) and has therefore no limits in terms of processing. It runs very fast due to using an efficient in-memory datastructure called [Flashtext](https://github.com/vi3k6i5/flashtext). It uses data from http://www.geonames.org/.

This project is mainly used in the context of decoding data from the "user.location" field of tweets but it can in principle be used on any address/location raw text field. Note that if you need very precise geographical information it is better to use one of the many available APIs. By default this repo only detects places with more than 30k inhabitants.

I have compared the predictions by local-geocode with geopy for 500 Twitter user locations. Local-geocode performs signficantly better (85% accuracy) than geopy (64% accuracy) for this use case. Read more about the benchmark [here](benchmark/benchmark.md).

# Install
```
pip install local-geocode
```

# Example usage
Local-geocode is able to parse arbitrary location names in many languages, as well as numerous alternative names of places and returns geographic information.

```python
from geocode.geocode import Geocode

gc = Geocode()
gc.load()  # load geonames data

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
```

# Usage
The easiest way to integrate `local-geocode` to your project is to simply run `pip install local-geocode`. You can also simply clone this repository and copy the folder `geocode` into your project. 

## Configuration
When installed with pip, local-geocode comes packaged with 2 pickle files which were generated using the default configuration. You can however change the configuration and then re-compute the pickle files for your needs.

The `Geocode()` initializer accepts the following arguments:
* `min_population_cutoff` (default: 30k): Places below this population size are excluded
* `large_city_population_cutoff` (default: 200k): Cities with a population size larger than this will be prioritized. Example: "Los Angeles, USA" will result in "Los Angeles" as the first result, and not "USA".
* `location_types`: Provide a list of location types which you would like to filter. By default it uses all location types (i.e. `['city', 'place', 'country', 'admin1', 'admin2', 'admin3', 'admin4', 'admin5', 'admin6', 'admin_other', 'continent', 'region']`).

Example:
```python
from geocode.geocode import Geocode

gc = Geocode(min_population_cutoff=100000)
gc.load()  # downloads geonames data (~1.2GB), parses data, generates pickle files in <package folder>/geocode/data for new configuration
```
(This may take 1-2min to run)


## Prioritization
If multiple locations are detected in an input string, local-geocode sorts the output by the following prioritization:
1. Large cities (`population size > large_city_population_cutoff`)
2. States/provinces (admin level 1)
3. Countries
4. Places (`population size <= large_city_population_cutoff`)
5. Counties (admin levels > 1)
6. Continents
7. Regions

## Parallelized
If you have a large number of texts to decode, it might make sense to use `decode_parallel` which runs decode in parallel:
```python
gc = Geocode()
gc.load()  # load geonames data

# a large number of items
mydata = ['Tel Aviv', ..,]
num_cpus = None # By default use all CPUs

locations = gc.decode_parallel(mydata, num_cpus=num_cpus)
print(locations)
```

# Contact
Please open an issue, if you run into problems!
