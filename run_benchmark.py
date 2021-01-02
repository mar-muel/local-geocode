from geocode.geocode import Geocode
from tqdm import tqdm
import pandas as pd
import numpy as np
import ast
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import os
import logging

logging.basicConfig(level=logging.INFO, format=',%(asctime)s [%(levelname)-5.5s] [%(name)-12.12s]: %(message)s')
logger = logging.getLogger(__name__)

benchmark_path = 'benchmark'
f_out_results = os.path.join(benchmark_path, 'benchmark_results.csv')
f_in = os.path.join(benchmark_path, 'benchmark_data.csv')

def read_benchmark_data():
    df = pd.read_csv(f_in)
    df['true'] = df.true.apply(lambda s: [np.nan] if s == '[nan]' else ast.literal_eval(s))
    return df

def predict_local_geocode(df):
    gc = Geocode()
    gc.prepare(recompute=False)
    gc.init()
    df['predicted'] = np.nan
    df['is_correct'] = False
    for i, row in tqdm(df.iterrows(), total=len(df)):
        res = gc.decode(row['user.location'])
        pred = np.nan
        if len(res) > 0:
            pred = res[0]['country_code']
        df.loc[i, 'predicted'] = pred
        df.loc[i, 'is_correct'] = pred in row['true']
    acc = df.is_correct.sum()/len(df)
    logger.info(f'Local-geocode accuracy: {acc:.3f}')
    return df

def predict_geopy(df, recompute=False):
    if os.path.isfile(f_out_results) or recompute:
        df_res = pd.read_csv(f_out_results)
        df['predicted_geopy'] = df_res['predicted_geopy']
        df['is_correct_geopy'] = df_res['is_correct_geopy']
    else:
        geolocator = Nominatim(user_agent="my-application-1234")
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        for i, row in tqdm(df.iterrows(), total=len(df)):
            res = geocode(row['user.location'], addressdetails=True, exactly_one=True)
            if res is None:
                res = np.nan
            else:
                res = res.raw['address']['country_code'].upper()
            df.loc[i, 'predicted_geopy'] = res
            df.loc[i, 'is_correct_geopy'] = res in row['true']
    acc = df.is_correct_geopy.sum()/len(df)
    logger.info(f'Nomatim/geopy accuracy: {acc:.3f}')
    return df

if __name__ == "__main__":
    df = read_benchmark_data()
    df = predict_geopy(df)
    df = predict_local_geocode(df)
    df.to_csv(f_out_results, index=False)
