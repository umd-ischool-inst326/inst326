from argparse import ArgumentParser
import re
import sys


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


def get_birthdays(filename):
    """ Extract names and birthdays from the provided text file. """
    info = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            name_match = re.search(
                r"""^\d+\.\s   # Match the line number
                (.*?)          # Match the name
                (:|'|\swas)    # Match the edge of the string
                """, line, flags=re.VERBOSE)
            
            if not name_match:
                # if there's no name, just keep going
                continue
            
            date1 = re.search(
                r"""(January|February|March|April|May|June|July|
                        August|September|October|November|December) # Match a full month
                \s                                               # Match a space
                (\d+|first|twenty-eighth)                        # Match the day
                """, line, flags=re.VERBOSE)
            
            date2 = re.search(
                r"""(Jan\.|Feb\.|Mar\.|Apr\.|May|Jun\.|
                        Jul\.|Aug\.|Sep\.|Oct\.|Nov\.|Dec\.) # Match an abbreviated month
                \s                                        # Match a space
                (\d+)                                     # Match the day
                """, line, flags=re.VERBOSE)
            
            date3 = re.search(
                r"""(\d+)   # Match a month number
                /           # Match a forward slash
                (\d+)       # Match a day number
                """, line, flags=re.VERBOSE)
            
            # this is just a sanity check:
            if not date1 and not date2 and not date3:
                raise ValueError(f"failed to parse {line}")
            
            name = name_match.group(1)
            month, day = (parse_date1(date1.group(1), date1.group(2)) if date1 else
                          parse_date2(date2.group(1), date2.group(2)) if date2 else
                          parse_date3(date3.group(1), date3.group(2)))
            info.append((name, month, day))
    return info


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
