""" Find the county in the specified state with the highest education level. """

from argparse import ArgumentParser
import pandas as pd
import sys


def most_educated(filepath, state):
    """ Find the county in the specified state with the highest education level.
    
    Args:
        filepath (str): path to education_by_county.csv
        state (str): two-letter state code
    
    Returns:
        str: the name of the county with the highest education level.
    """
    df = pd.read_csv(filepath)
    state_df = df[df["State"] == state]
    col = "Percent of adults with a bachelor's degree or higher"
    percent = state_df[col].max()
    county = state_df[state_df[col] == percent]["Area name"].iloc[0]
    return county, percent


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to CSV file")
    parser.add_argument("state", help="two-letter state code")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    county, percent = most_educated(args.filepath, args.state)
    print(f"{percent}% of adults in {county} have at least a bachelor's degree")
