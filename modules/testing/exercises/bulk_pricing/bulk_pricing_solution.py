""" Calculate the price of an order of magnets according to a bulk
pricing scheme. """

import sys


def get_cost(magnets):
    if magnets < 0:
        raise ValueError("number of magnets must be non-negative")
    price = (0.75 if magnets <   50 else
             0.72 if magnets <  100 else
             0.70 if magnets < 1000 else
             0.67)
    return price * magnets


if __name__ == "__main__":
    try:
        magnets = int(sys.argv[1])
    except IndexError:
        sys.exit("this program expects a number of magnets as a command-line"
                 " argument")
    except ValueError:
        sys.exit("could not convert " + sys.argv[1] + " into an integer")
    print(get_cost(magnets))
