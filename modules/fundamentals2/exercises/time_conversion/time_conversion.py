""" Convert times from 24-hour format to 12-hour format with times of day. """

from argparse import ArgumentParser
import sys


# replace this comment with your implementation of the convert_times() function


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("hours", nargs="+", type=int, choices=range(0, 24),
                        help="hours to convert")
    args = parser.parse_args(sys.argv[1:])
    converted = convert_times(args.hours)
    assert len(converted) == len(args.hours), \
        "return value of convert_times() contains the wrong number of items"
    for original, conv in zip(args.hours, converted):
        print(f"{original} in 24-hour time is {conv}")
