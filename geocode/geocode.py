import pandas as pd
import os
import pickle
import logging
import numpy as np
from tqdm import tqdm
import numpy as np
import multiprocessing
import joblib
import ast
import shapely.geometry
import sys
from flashtext import KeywordProcessor

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)-5.5s] [%(name)-12.12s]: %(message)s')
log = logging.getLogger(__name__)

class Geocode():
    """
    Geocode

    Download geo dataset from:
    - https://download.geonames.org/export/dump/allCountries.zip
    - https://download.geonames.org/export/dump/featureCodes_en.txt
    """

    def __init__(self, with_altnames=False):
        self.with_altnames = with_altnames
        self.kp = None
        self.geo_data = None

    def init(self):
        self.kp = self.get_keyword_processor_pickle()
        self.geo_data = self.get_geonames_pickle()

    def get_geonames_data(self):
        geonames_data_path = os.path.join('.', 'data', 'allCountries.txt')
        if not os.path.isfile(geonames_data_path):
            raise FileNotFoundError(f'File {geonames_data_path} is not present! Download it first from https://download.geonames.org/export/dump/allCountries.zip')
        dtypes = {'name': str, 'latitude': float, 'longitude': float, 'country_code': str, 'population': int, 'feature_code': str}
        if self.with_altnames:
            dtypes['alternatenames'] = str
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
        with_altnames_tag = '_with_altnames' if self.with_altnames else ''
        cache_path = self.get_cache_path(f'geonames{with_altnames_tag}.pkl')
        return cache_path

    @property
    def keyword_processor_pickle_path(self):
        with_altnames_tag = '_with_altnames' if self.with_altnames else ''
        cache_path = self.get_cache_path(f'geonames_keyword_processor_{with_altnames_tag}.pkl')
        return cache_path

    def get_cache_path(self, name):
        return os.path.join('.', 'data', name)

    def get_geonames_pickle(self):
        with open(self.geonames_pickle_path, 'rb') as f:
            df = pickle.load(f)
        return df

    def get_keyword_processor_pickle(self):
        with open(self.keyword_processor_pickle_path, 'rb') as f:
           kp = pickle.load(f)
        return kp

    def create_geonames_pickle(self):
        log.info('Transforming geonames data...')
        log.info('Reading geo data...')
        df = self.get_geonames_data()
        # select places with a population greater zero
        df = df[df.population > 0]
        # get rid of administrative zones without country codes (e.g. "The Commonwealth")
        df = df[~df.country_code.isnull()]
        # select places with feature class A (admin) and P (place)
        df_features = self.get_feature_names_data()
        df = df.merge(df_features, on='feature_code', how='left')
        df = df[df.feature_code_class.isin(['A', 'P'])]
        # generate list of priorities by ID. Levels of priority:
        # - Places are given priority over admin areas
        # - Among places, sort by "importance of a place" (PPL > PPLA > PPLA2, etc.)
        # - Among admin give priority to second order divisions over country names, after that priority decreases with area size (ADM2 > ADM1 > ADM3 > ADM4),
        # - Among feature class prioritize by population size
        log.info('Sorting by priority...')
        feature_code_priorities = ['PPL', 'PPLA', 'PPLA2', 'PPLA3', 'PPLA4', 'PPLA5', 'PPLC', 'PPLCH', 'PPLF', 'PPLG', 'PPLH', 'PPLL',
                'PPLQ', 'PPLR', 'PPLS', 'PPLW', 'PPLX', 'STLMT', 'ADM2', 'ADM2H', 'ADM1', 'ADM1H', 'ADM3', 'ADM3H', 'ADM4', 'ADM4H',
                'ADM5', 'ADM5H', 'ADMD', 'ADMDH', 'LTER', 'PCL', 'PCLD', 'PCLF', 'PCLH', 'PCLI', 'PCLIX', 'PCLS', 'PRSH', 'TERR', 'ZN', 'ZNB']
        feature_code_priorities = {k: i for i, k in enumerate(feature_code_priorities)}
        df['priority'] = df.feature_code.apply(lambda code: feature_code_priorities[code])
        df.sort_values(by=['priority', 'population'], ascending=[True, False], inplace=True)
        geo_coords = []
        # Build geo data array. Position i in list corresponds to priority
        log.info('Build coordinate data list...')
        for _, row in tqdm(df.iterrows(), total=len(df)):
            geo_coords.append([row['name'], row['country_code'], row['longitude'], row['latitude']])
            if self.with_altnames:
                if isinstance(row['alternatenames'], str):
                    altnames = row['alternatenames'].split(',')
                    for altname in altnames:
                        geo_coords.append([altname, row['country_code'], row['longitude'], row['latitude']])
        log.info('Writing geonames data to pickle...')
        with open(self.geonames_pickle_path, 'wb') as f:
            pickle.dump(geo_coords, f)

    def create_keyword_processor_pickle(self):
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
        """
        Transform raw data of country names into a list of coordinates (where the position i corresponds to the priority i of the element)
        """
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
        matches = sorted([int(m) for m in matches])
        field_names = ['name', 'country_code', 'longitude', 'latitude']
        return [dict(zip(field_names, self.geo_data[m])) for m in matches]
