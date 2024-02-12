from geocode.geocode import Geocode
import argparse
import sys
import logging
import json

USAGE_DESC = """
python main.py <command> [<args>]

Available commands:
  prepare          Parses raw data from geonames into pickles
  decode           Runs geocoding on input text
"""

def parse_list_of_strs(arg):
    return arg.split(',')


class ArgParseDefault(argparse.ArgumentParser):
    """Simple wrapper which shows defaults in help"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs, formatter_class=argparse.ArgumentDefaultsHelpFormatter)

class ArgParse(object):
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)-5.5s] [%(name)-12.12s]: %(message)s')
        parser = ArgParseDefault(
                description='',
                usage=USAGE_DESC)
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            sys.exit(1)
        getattr(self, args.command)()

    def prepare(self):
        parser = ArgParseDefault(description='Prepares raw data from geonames and outputs pickles')
        parser.add_argument('--min_population_cutoff', default=30000, required=False, type=int, help='Exclude all places below this cutoff')
        parser.add_argument('--large_city_population_cutoff', default=200000, required=False, type=int, help='Cities above this population will appear with higher in priority')
        parser.add_argument(
            '--country_code_in',
            default=[],
            required=False,
            type=parse_list_of_strs,
            help='Only places within these country codes will be included'
        )
        parser.add_argument('--recompute', default=False, action='store_true', help='Recompute pickles')
        args = parser.parse_args(sys.argv[2:])
        geocode = Geocode(
            min_population_cutoff=args.min_population_cutoff,
            large_city_population_cutoff=args.large_city_population_cutoff,
            country_code_in=args.country_code_in
        )
        geocode.load(recompute=args.recompute)

    def decode(self):
        parser = ArgParseDefault(description='Split annotated data into training and test data set')
        parser.add_argument('-i', '--input', dest='input_text', type=str, required=True, help='Input text to geocode')
        args = parser.parse_args(sys.argv[2:])
        geocode = Geocode()
        geocode.load()
        decoded = geocode.decode(args.input_text)
        print(json.dumps(decoded))


if __name__ == '__main__':
    ArgParse()
