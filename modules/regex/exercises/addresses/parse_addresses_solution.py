from argparse import ArgumentParser
import re
import sys


def parse_address(line):
    """ Break down line into a house number, a street, a city, a state,
    and a zip code.
    
    Args:
        line (str): the string to parse.
    
    Returns:
        (dict of str: str): A dictionary with the keys "house_number",
        "street", "city", "state", and "zip". If the line could not be
        parsed, returns None.
    """
    expr = re.compile(r"^(\S+)\s([^,]+),\s(.*)\s([A-Z]{2})\s(\d{5})$")
    match = expr.search(line)
    # note: it's not necessary to use re.compile(); students can just do
    # match = re.search(r"^(\S+)\s([^,]+),\s(.*)\s([A-Z]{2})\s(\d{5})$", line)
    return {
        "house_number": match.group(1),
        "street": match.group(2),
        "city": match.group(3),
        "state": match.group(4),
        "zip": match.group(5)
    } if match else None


def parse_addresses(filename):
    """ Parse addresses into a list of dictionaries.
    
    Args:
        filename (str): path to a file containing one address per line.
    
    Returns:
        list of dict: a list of dictionaries with one dictionary per
        address. For the format of each dictionary, see parse_address()
        above.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return [parse_address(l) for l in f]


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file",
                        help="file containing one address per line")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in parse_addresses(args.file):
        print(address)
