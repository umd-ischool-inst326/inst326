"""Calculate Gregorian Easter using Gauss's algorithm."""

import sys

def easter_date(y):
    """ Calculate Gregorian Easter using Gauss's algorithm.
    
    Args:
        y (int): the year to calculate Easter for.

    Returns:
        (str): the date of Easter in the specified year.
    """
    if y < 1583:
        raise ValueError("Year must be at least 1583")
    a = y % 19
    b = y % 4
    c = y % 7
    k = y // 100
    p = (13 + 8*k) // 25
    q = k // 4
    M = (15 - p + k - q) % 30
    N = (4 + k - q) % 7
    d = (19*a + M) % 30
    e = (2*b + 4*c + 6*d + N) % 7
    march = 22 + d + e
    april = d + e - 9
    if d == 29 and e == 6 and april == 26:
        april = 19
    if d == 28 and (11*M + 11) % 30 < 19 and april == 25:
        april = 18
    date = f"March {march}" if march < 32 else f"April {april}"
    return date


if __name__ == "__main__":
    try:
        year = int(sys.argv[1])
    except IndexError:
        for i in range(1583, 2100):
            # print(i, easter_date(i))
            easter_date(i)
        # sys.exit("this program expects a year as a command-line argument")
    except ValueError:
        sys.exit("could not convert", sys.argv[1], "into an integer")
    else:
        print(easter_date(year))
