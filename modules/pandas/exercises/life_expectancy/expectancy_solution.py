from argparse import ArgumentParser
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys


def plot_life_expectancy(csv_file, column):
    """Plot life expectancy against another factor using a Seaborn joint plot.
    
    Args:
        csv_file (str): path to a CSV file containing life expectancy data.
        column (str): name of a column in the CSV file containing numeric data.
    
    Side effects:
        Displays a joint plot of life expectancy vs. the selected column.
    """
    df = pd.read_csv(csv_file)
    sns.jointplot(data=df[df["Year"]==2015], x="Life expectancy", y=column,
                  hue="Status")
    plt.show()


def parse_args(arglist):
    """Parse command-line arguments.
    
    Two arguments are expected: the path to a CSV file containing life
    expectancy data, and the name of a column in the file containing numeric
    values.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with attributes csv_file and column (both strings).
    """
    parser = ArgumentParser()
    parser.add_argument("csv_file", help="path to life expectancy CSV file")
    parser.add_argument("column", help="name of column in dataset")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    plot_life_expectancy(args.csv_file, args.column)