from argparse import ArgumentParser
import requests
import sys


def get_holidays(countrycode, year):
    """ Retrieve and display holidays from https://date.nager.at. """
    url = f"https://date.nager.at/Api/v1/Get/{countrycode}/{year}"
    response = requests.get(url)
    for holiday in response.json():
        print(f"{holiday['date']}: {holiday['name']}")
        

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("countrycode", help="two-character country code")
    parser.add_argument("year", type=int, help="four-digit year")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    get_holidays(args.countrycode, args.year)
