""" Convert times from 24-hour format to 12-hour format with times of day. """

from argparse import ArgumentParser
import sys


def convert_times(hours):
    result = []
    for hour in hours:
        result.append(
            "12 midnight" if hour == 0 else
            "12 noon" if hour == 12 else
            f"{hour} in the morning" if hour < 12 else
            f"{hour - 12} in the afternoon" if hour < 17 else
            f"{hour - 12} in the evening" if hour < 21 else
            f"{hour - 12} at night"
        )
    return result


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
