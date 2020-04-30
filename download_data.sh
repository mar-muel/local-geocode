wget https://download.geonames.org/export/dump/allCountries.zip -P ./data/
unzip ./data/allCountries.zip -d ./data/ && rm ./data/allCountries.zip
wget https://download.geonames.org/export/dump/featureCodes_en.txt -P ./data/
