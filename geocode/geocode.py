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

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)-5.5s] [%(name)-12.12s]: %(message)s')
log = logging.getLogger(__name__)

class Geocode():
    """
    Geocode

    Download geo dataset from:
    - https://download.geonames.org/export/dump/allCountries.zip
    - https://download.geonames.org/export/dump/featureCodes_en.txt
    """

    def __init__(self, min_population_cutoff=30000, large_city_population_cutoff=200000):
        self.kp = None
        self.geo_data = None
        self.min_population_cutoff = min_population_cutoff
        self.large_city_population_cutoff = large_city_population_cutoff

    def init(self):
        self.kp = self.get_keyword_processor_pickle()
        self.geo_data = self.get_geonames_pickle()

    def get_geonames_data(self):
        geonames_data_path = os.path.join('.', 'data', 'allCountries.txt')
        if not os.path.isfile(geonames_data_path):
            raise FileNotFoundError(f'File {geonames_data_path} is not present! Download it first from https://download.geonames.org/export/dump/allCountries.zip')
        dtypes = {'name': str, 'latitude': float, 'longitude': float, 'country_code': str, 'population': int, 'feature_code': str, 'alternatenames': str}
        geonames_columns = ['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude', 'feature_class', 'feature_code', 'country_code', 'cc2', 'admin1', 'admin2', 'admin3', 'admin4', 'population', 'elevation', 'dem', 'timezone', 'modification_date']
        df = pd.read_csv(geonames_data_path, names=geonames_columns, sep='\t', dtype=dtypes, usecols=dtypes.keys())
        return df

    def get_feature_names_data(self):
        feature_code_path = os.path.join('.', 'data', 'featureCodes_en.txt')
        if not os.path.isfile(feature_code_path):
            raise FileNotFoundError(f'File {feature_code_path} is not present! Download it first from https://download.geonames.org/export/dump/featureCodes_en.txt')
        df_features = pd.read_csv(feature_code_path, sep='\t', names=['feature_code', 'description-short', 'description-long'])
        df_features['feature_code_class'] = ''
        df_features.loc[:, ['feature_code_class', 'feature_code']] = df_features.feature_code.str.split('.', expand=True).values
        return df_features

    @property
    def geonames_pickle_path(self):
        cache_path = self.get_cache_path(f'geonames.pkl')
        return cache_path

    @property
    def keyword_processor_pickle_path(self):
        cache_path = self.get_cache_path(f'geonames_keyword_processor.pkl')
        return cache_path

    def get_cache_path(self, name):
        return os.path.join('/', 'tmp', name)

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
        log.info('Transforming geonames data...')
        log.info('Reading geo data...')
        df = self.get_geonames_data()
        # select places with a population greater zero
        df = df[(df.population > 0) | (df.feature_code == 'PCLI')]
        # get rid of administrative zones without country codes (e.g. "The Commonwealth")
        df = df[~df.country_code.isnull()]
        # select places with feature class A (admin) and P (place)
        df_features = self.get_feature_names_data()
        df = df.merge(df_features, on='feature_code', how='left')
        df = df[df.feature_code_class.isin(['A', 'P'])]
        # Filter out everything below a certain popluation
        df = df[df['population'] > self.min_population_cutoff]
        # expand alternate names
        df.loc[:, 'alternatenames'] = df.alternatenames.str.split(',')
        df['is_altname'] = False
        _df = df.explode('alternatenames')
        _df['name'] = _df['alternatenames']
        _df['is_altname'] = True
        df = pd.concat([df, _df])
        # Remove all names that are floats/ints
        df['is_str'] = df.name.apply(lambda s: isinstance(s, str))
        df = df[df['is_str']]
        # Levels of priority:
        # 1) Prioritize large cities (population size > large_city_population_cutoff)
        # 2) Admin areas
        # 3) Places
        # Within each group we will sort according to population size
        log.info('Sorting by priority...')
        feature_code_priorities = ['A', 'P']
        df.loc[(df.population > self.large_city_population_cutoff) & (df.feature_code_class == 'P') & (~df.is_altname), 'priority'] = 0
        feature_code_priorities = {k: i+1 for i, k in enumerate(feature_code_priorities)}
        df['priority'] = df.feature_code_class.apply(lambda code: feature_code_priorities[code])
        # Only allow 2 character names in specific cases
        # - Name is non-ascii (e.g. Chinese characters)
        # - Is an alternative name for a country (e.g. UK)
        # - Is a US state or Canadian province
        df['is_ascii'] = df.name.apply(is_ascii)
        df['is_country'] = df.feature_code.str.startswith('PCL')
        df = df[
                (~df.is_ascii) | 
                (df.name.str.len() > 2) | 
                ((df.name.str.len() == 2) & (df.country_code == 'US')) |
                ((df.name.str.len() == 2) & (df.country_code == 'CA')) |
                ((df.name.str.len() == 2) & (df.is_country))
                ]
        # add "US" manually since it's missing in geonames
        row_usa = df[df.is_country & (df.name == 'USA')].iloc[0]
        row_usa['name'] = 'US'
        df = df.append(row_usa)
        # sort by priorities and drop name duplicates (this way we will keep only the high priority elements)
        df.sort_values(by=['priority', 'population'], ascending=[True, False], inplace=True)
        df['name_lower'] = df.name.str.lower()
        df = df.drop_duplicates('name_lower', keep='first')
        log.info(f'... collected a total of {len(df):,} names of places and countries')
        # Build geo data array. Position in list corresponds to priority
        log.info('Writing geonames data to pickle...')
        df = df[['name', 'country_code', 'longitude', 'latitude']].values.tolist()
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
        log.info('Writing keyword processor pickle...')
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
        field_names = ['name', 'country_code', 'longitude', 'latitude']
        return [dict(zip(field_names, self.geo_data[m])) for m in matches]

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
        log.info(f'Running decode in parallel with {num_cpus} cores')
        process_chunk_delayed = joblib.delayed(process_chunk)
        result = joblib.Parallel(n_jobs=num_cpus)(process_chunk_delayed(chunk, self) for chunk in tqdm(np.array_split(input_texts, num_cpus)))
        return [r for res in result for r in res]

