""" Calculate the price of an order of magnets according to a bulk
pricing scheme. """

import sys


# replace this comment with your implementation of the get_cost() function


if __name__ == "__main__":
    try:
        magnets = int(sys.argv[1])
    except IndexError:
        sys.exit("this program expects a number of magnets as a command-line"
                 " argument")
    except ValueError:
        sys.exit("could not convert " + sys.argv[1] + " into an integer")
    print(get_cost(magnets))
