import pandas as pd
import os
import pickle
import logging
from tqdm import tqdm
import sys
from flashtext import KeywordProcessor
import joblib
import multiprocessing
import numpy as np
import urllib.request
import zipfile
import numpy as np
import hashlib
import getpass
import json


logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)-5.5s] [%(name)-12.12s]: %(message)s')
log = logging.getLogger(__name__)

class Geocode():
    """
    Geocode

    Download geo dataset from:
    - https://download.geonames.org/export/dump/allCountries.zip
    - https://download.geonames.org/export/dump/featureCodes_en.txt
    """

    def __init__(self, min_population_cutoff=30000, large_city_population_cutoff=200000, location_types=None):
        self.kp = None
        self.geo_data = None
        self.min_population_cutoff = min_population_cutoff
        self.large_city_population_cutoff = large_city_population_cutoff
        self.geo_data_field_names = ['name', 'official_name', 'country_code', 'longitude', 'latitude', 'geoname_id', 'location_type', 'population']
        self.default_location_types = ['city', 'place', 'country', 'admin1', 'admin2', 'admin3', 'admin4', 'admin5', 'admin6', 'admin_other', 'continent', 'region']
        self.location_types = self._get_location_types(location_types)
        self.argument_hash = self.get_arguments_hash()

    def init(self):
        self.kp = self.get_keyword_processor_pickle()
        self.geo_data = self.get_geonames_pickle()

    def get_geonames_data(self):
        geonames_data_path = self.get_cache_path('allCountries.txt')
        if not os.path.isfile(geonames_data_path):
            # download file
            url = 'https://download.geonames.org/export/dump/allCountries.zip'
            log.info(f'Downloading data from {url}')
            geonames_data_path_zip = self.get_cache_path('allCountries.zip')
            urllib.request.urlretrieve(url, geonames_data_path_zip)
            log.info(f'... done')
            log.info('Extracting data...')
            # extract
            with zipfile.ZipFile(geonames_data_path_zip, 'r') as f:
                f.extractall(self.tmp_dir)
            log.info('...done')
            # remove zip file
            os.remove(geonames_data_path_zip)
        log.info(f'Reading data from {geonames_data_path}...')
        dtypes = {'name': str, 'latitude': float, 'longitude': float, 'country_code': str, 'population': int, 'feature_code': str, 'alternatenames': str, 'geoname_id': str}
        geonames_columns = ['geoname_id', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude', 'feature_class', 'feature_code', 'country_code', 'cc2', 'admin1', 'admin2', 'admin3', 'admin4', 'population', 'elevation', 'dem', 'timezone', 'modification_date']
        df = pd.read_csv(geonames_data_path, names=geonames_columns, sep='\t', dtype=dtypes, usecols=dtypes.keys())
        # remove data file
        # os.remove(geonames_data_path)
        return df

    def get_feature_names_data(self):
        feature_code_path = self.get_cache_path('featureCodes_en.txt')
        if not os.path.isfile(feature_code_path):
            # download file
            url = 'https://download.geonames.org/export/dump/featureCodes_en.txt'
            log.info(f'Downloading data from {url}')
            urllib.request.urlretrieve(url, feature_code_path)
            log.info(f'... done')
        log.info(f'Reading data from {feature_code_path}...')
        df_features = pd.read_csv(feature_code_path, sep='\t', names=['feature_code', 'description-short', 'description-long'])
        df_features['feature_code_class'] = ''
        df_features.loc[:, ['feature_code_class', 'feature_code']] = df_features.feature_code.str.split('.', expand=True).values
        # remove data file
        # os.remove(feature_code_path)
        return df_features

    @property
    def geonames_pickle_path(self):
        cache_path = self.get_cache_path(f'geonames_{self.argument_hash}.pkl')
        return cache_path

    @property
    def keyword_processor_pickle_path(self):
        cache_path = self.get_cache_path(f'geonames_keyword_processor{self.argument_hash}.pkl')
        return cache_path

    @property
    def tmp_dir(self):
        return os.path.join('/', 'tmp', 'local_geocode')

    def get_cache_path(self, name):
        if not os.path.isdir(self.tmp_dir):
            os.makedirs(self.tmp_dir)
        return os.path.join(self.tmp_dir, name)

    def get_geonames_pickle(self):
        with open(self.geonames_pickle_path, 'rb') as f:
            df = pickle.load(f)
        return df

    def get_keyword_processor_pickle(self):
        with open(self.keyword_processor_pickle_path, 'rb') as f:
           kp = pickle.load(f)
        return kp

    def create_geonames_pickle(self):
        """Create list of place/country data from geonames data and sort according to priorities"""
        def is_ascii(s):
            try:
                s.encode(encoding='utf-8').decode('ascii')
            except UnicodeDecodeError:
                return False
            else:
                return True
        log.info('Reading geo data...')
        df = self.get_geonames_data()

        # Global filtering 
        log.info('Reading feature class data...')
        df_features = self.get_feature_names_data()
        df = df.merge(df_features, on='feature_code', how='left')
        df.loc[df.geoname_id == '3355338', 'country_code'] = 'NA' # strangely, Namibia is missing the country_code
        # Apply the following filters:
        # - only keep places with feature class A (admin) and P (place), and CONT (continent)
        df = df[
                (df.feature_code_class.isin(['A', 'P'])) |
                (df.feature_code.isin(['CONT', 'RGN']))
                ]
        # - remove everything below min_population_cutoff
        df = df[
                (df['population'] > self.min_population_cutoff) | 
                (df.feature_code.isin(['CONT', 'RGN']))
                ]
        # - get rid of items without a country code, usually administrative zones without country codes (e.g. "The Commonwealth")
        df = df[
                (~df.country_code.isnull()) |
                (df.feature_code.isin(['CONT', 'RGN']))
                ]
        # - remove certain administrative regions (such as zones, historical divisions, territories)
        df = df[~df.feature_code.isin(['ZN', 'PCLH', 'TERR'])]

        # Expansion of altnames
        df['official_name'] = df['name']
        # - expand alternate names
        df.loc[:, 'alternatenames'] = df.alternatenames.str.split(',')
        df['is_altname'] = False
        _df = df.explode('alternatenames')
        _df['name'] = _df['alternatenames']
        _df['is_altname'] = True
        df = pd.concat([df, _df])
        df = df.drop(columns=['alternatenames'])
        log.info(f'... read a total of {len(df):,} location names')

        # Filtering applied to names and altnames
        log.info('Apply filters...')
        # - remove all names that are floats/ints
        df['is_str'] = df.name.apply(lambda s: isinstance(s, str))
        df = df[df['is_str']]
        # - only allow 2 character names if 1) name is non-ascii (e.g. Chinese characters) 2) is an alternative name for a country (e.g. UK) 
        #   3) is a US state or Canadian province
        df['is_country'] = df.feature_code.str.startswith('PCL')
        df['is_ascii'] = df.name.apply(is_ascii)
        # add "US" manually since it's missing in geonames
        row_usa = df[df.is_country & (df.name == 'USA')].iloc[0]
        row_usa['name'] = 'US'
        df = df.append(row_usa)
        df = df[
                (~df.is_ascii) | 
                (df.name.str.len() > 2) | 
                ((df.name.str.len() == 2) & (df.country_code == 'US')) |
                ((df.name.str.len() == 2) & (df.country_code == 'CA')) |
                ((df.name.str.len() == 2) & (df.is_country))
                ]
        # - altnames need to have at least 4 characters (removes e.g. 3-letter codes)
        df = df[~(
                    (~df.is_country) &
                    (~df.country_code.isin(['US', 'CA'])) &
                    (df.is_ascii) &
                    (df.is_altname) &
                    (df.name.str.len() < 4)
                    )]
        # - remove altnames of insignificant admin levels and of places that are very small
        # set admin level
        df['admin_level'] = None
        df.loc[df.feature_code.isin(['PCLI', 'PCLD', 'PCLF', 'PCLS', 'PCLIX', 'PCLX', 'PCL']), 'admin_level'] = 0
        for admin_level in range(1, 6):
            df.loc[df.feature_code.isin([f'ADM{admin_level}', f'ADM{admin_level}H']), 'admin_level'] = admin_level
        df = df[
                ~(
                    ((df.is_altname) & (df.admin_level.isin([3,4,5]))) |
                    ((df.is_altname) & (df.feature_code_class == 'P') & (df.population < 100000))
                    )
                ]

        # Add flags
        flags = self.read_flag_data()
        df_countries = df[(df.geoname_id.isin([str(v) for v in flags.values()])) & (~df.is_altname)].copy()
        for flag, geoname_id in flags.items():
            try:
                row = df_countries[(df_countries.geoname_id == str(geoname_id))].iloc[0].copy()
            except IndexError:
                pass
            else:
                row['name'] = flag
                df = df.append(row)

        # Sort by priorities and drop duplicate names
        # Priorities
        # 1) Large cities (population size > large_city_population_cutoff)
        # 2) States/provinces (admin_level == 1)
        # 3) Countries (admin_level = 0)
        # 4) Places
        # 5) counties (admin_level > 1)
        # 6) continents
        # 7) regions
        # (within each group we will sort according to population size)
        # Assigning priorities
        df['priority'] = np.nan
        df.loc[(df.feature_code == 'RGN'), 'priority'] = 7
        df.loc[(df.feature_code == 'CONT'), 'priority'] = 6
        df.loc[(df.feature_code_class == 'A') & (df.admin_level > 1), 'priority'] = 5
        df.loc[df.feature_code_class == 'P', 'priority'] = 4
        df.loc[(df.feature_code_class == 'A') & (df.admin_level == 0), 'priority'] = 3
        df.loc[(df.feature_code_class == 'A') & (df.admin_level == 1), 'priority'] = 2
        df.loc[(df.population > self.large_city_population_cutoff) & (df.feature_code_class == 'P') & (~df.is_altname), 'priority'] = 1
        # Sorting
        log.info('Sorting by priority...')
        df.sort_values(by=['priority', 'population'], ascending=[True, False], inplace=True)
        # drop name duplicates by keeping only the high priority elements
        df['name_lower'] = df['name'].str.lower()
        df = df.drop_duplicates('name_lower', keep='first')
        # set location_types
        df['location_type'] = np.nan
        for admin_level in range(1, 6):
            df.loc[df.admin_level == admin_level, 'location_type'] = f'admin{admin_level}'
        df.loc[df.feature_code == 'ADMD', 'location_type'] = 'admin_other'
        df.loc[df.admin_level == 0, 'location_type'] = 'country'
        df.loc[(df.population <= self.large_city_population_cutoff) & (df.feature_code_class == 'P'), 'location_type'] = 'place'
        df.loc[(df.population > self.large_city_population_cutoff) & (df.feature_code_class == 'P'), 'location_type'] = 'city'
        df.loc[df.feature_code == 'CONT', 'location_type'] = 'continent'
        df.loc[df.feature_code == 'RGN', 'location_type'] = 'region'
        if len(df[df.location_type.isna()]) > 0:
            log.warning(f'{len(df[df.location_type.isna()]):,} locations could not be matched to a location_type. These will be ignored.')
        # filter by user-defined location types
        df = df[df.location_type.isin(self.location_types)]
        location_types_counts = dict(df.location_type.value_counts())
        log.info(f'Collected a total of {len(df):,} location names. Breakdown by location types:')
        for loc_type, loc_type_count in location_types_counts.items():
            log.info(f'... type {loc_type}: {loc_type_count:,}')
        # Write as pickled list
        log.info(f'Writing geonames data to file {self.geonames_pickle_path}...')
        df = df[self.geo_data_field_names].values.tolist()
        with open(self.geonames_pickle_path, 'wb') as f:
            pickle.dump(df, f)

    def create_keyword_processor_pickle(self):
        """Builds trie lookup data structure for name lookup. This maps input names to position IDs."""
        geo_data = self.get_geonames_pickle()
        kp = KeywordProcessor()
        log.info('Adding terms to keyword processor (building trie)...')
        for i, item in tqdm(enumerate(geo_data), total=len(geo_data)):
            idx = str(i)
            kp.add_keyword(item[0], idx)
        log.info(f'Writing keyword processor pickle to file {self.keyword_processor_pickle_path}...')
        with open(self.keyword_processor_pickle_path, 'wb') as f:
            pickle.dump(kp, f)

    def prepare(self, recompute=False):
        """Prepare data pickles"""
        # geonames data
        if os.path.isfile(self.geonames_pickle_path) and not recompute:
            log.info('Pickled geonames file is already present!')
        else:
            self.create_geonames_pickle()
        # keyword processor
        if os.path.isfile(self.keyword_processor_pickle_path) and not recompute:
            log.info('Pickled keyword processor file is already present!')
        else:
            self.create_keyword_processor_pickle()
        log.info('... You are all set!')

    def decode(self, input_text):
        matches = self.kp.extract_keywords(input_text)
        if len(matches) == 0:
            return []
        # sort by priorities
        matches = sorted(list(set(int(m) for m in matches)))
        return [dict(zip(self.geo_data_field_names, self.geo_data[m])) for m in matches]

    def decode_parallel(self, input_texts, num_cpus=None):
        """Run decode in parallel"""
        def process_chunk(chunk, gc):
            gc.init()  # load pickles
            results = []
            for item in tqdm(chunk, total=len(chunk)):
                res = gc.decode(item)
                results.append(res)
            return results

        if num_cpus is None:
            num_cpus = max(multiprocessing.cpu_count() - 1, 1)
        else:
            num_cpus = max(num_cpus, 1)
        # remove pickles from memory
        self.kp = None
        self.geo_data = None 
        log.info(f'Running decode in parallel with {num_cpus} cores')
        process_chunk_delayed = joblib.delayed(process_chunk)
        result = joblib.Parallel(n_jobs=num_cpus)(process_chunk_delayed(chunk, self) for chunk in tqdm(np.array_split(input_texts, num_cpus)))
        return [r for res in result for r in res]

    def get_arguments_hash(self):
        geocode_args = [str(self.min_population_cutoff), str(self.large_city_population_cutoff)] + self.location_types
        # append username
        geocode_args.append(getpass.getuser())
        return hashlib.sha256(','.join(geocode_args).encode()).hexdigest()[:15]

    def read_flag_data(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(this_dir, 'flags.json'), 'r') as f:
            flags = json.load(f)
        return flags

    # private

    def _get_location_types(self, location_types):
        if location_types is None:
            return self.default_location_types
        _location_types = []
        for _t in location_types:
            if _t not in self.default_location_types:
                log.warning(f'Location type {_t} will be ignored as it is not part of the default location types ({",".join(self.default_location_types)})')
                continue
            _location_types.append(_t)
        return _location_types

