from argparse import ArgumentParser
import re
import sys


# Replace this comment with your implementation of get_birthdays().


def parse_date1(month, day):
    """ Parse a date like "January first" or "July 11".
    
    Args:
        month (str): an unabbreviated month.
        day (str): a day, expressed as a number (e.g., "28") or a word.
            This function only knows the words "first" and
            "twenty-eighth".
    
    Returns:
        tuple of int, int: the month and day as integers.
    """
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November",
              "December"]
    month_num = months.index(month) + 1
    day_num = 1 if day == "first" else 28 if day == "twenty-eighth" else int(day)
    return month_num, day_num


def parse_date2(month, day):
    """ Parse a date like "Oct. 18".
    
    Args:
        month (str): an abbreviated month (e.g., "Oct.").
        day (str): a day, expressed as a number (e.g., "28").
    
    Returns:
        tuple of int, int: the month and day as integers.
    """
    months = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.",
              "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    month_num = months.index(month) + 1
    day_num = int(day)
    return month_num, day_num


def parse_date3(month, day):
    """ Parse a date like "7/14".
    
    Args:
        month (str): a month, expressed as a number (e.g., "10").
        day (str): a day, expressed as a number (e.g., "28").
    
    Returns:
        tuple of int, int: the month and day as integers.
    """
    return int(month), int(day)


def main(filename):
    for name, month, day in get_birthdays(filename):
        print(name, month, day)


def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("filename", help="file containing celebrity birthdays")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)
