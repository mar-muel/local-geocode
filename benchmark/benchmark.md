# Comparison against geopy

This comparison shows how local-geocode and geopy (Nominatim) predict on a human-annotated set of 500 Twitter users locations. Each user location could be annotated with either `[nan]` (no real location provided) or a list of candidate countries if multiple countries were mentioned.

## Results
You can see the results [here](benchmark_results.csv). Local-geocode had an accuracy of 85% on this corpus, geopy 64%.

Main take-aways:
* Imaginary names are not predicted, whereas geopy assumes it is a real place and tries to predict something
* Local-geocode supports country codes for semi-autonomous countries (e.g. Hong Kong, Puerto Rico, etc.)
* Geopy does sometimes a better job when states are given (e.g. London, ON vs. London UK). However, geopy fails consistently in the case of "CA" for California 
* An error rate of zero is tricky due to the many name collisions. Tuning hyperparameters or limiting by certain countries would probably improve performance by a lot.
* This test is on the country-level. It is possible that geopy performs better on more fine-grained location (in particular when a full address is provided).
* Due to the rate-limiting of 1 sec per request, geopy takes more than 8min to run this benchmark, local-geocode runs in a few seconds.

## Run the benchmark
You can run the benchmark yourself using
```bash
python run_benchmark.py
```
in the project root.
