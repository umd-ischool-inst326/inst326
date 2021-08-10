from argparse import ArgumentParser
import sys


def check_brackets(line):
    """ Determine if the brackets in line are balanced.

    Args:
        line (str): a line of text.

    Returns:
        bool: True if the brackets in line are balanced, otherwise False.
    """
    stack = []
    for char in line:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char in [")", "}", "]"]:
            if len(stack) == 0:
                return False
            prev = stack.pop()
            if ((prev == "(" and not char == ")")
                or (prev == "{" and not char == "}")
                or (prev == "[" and not char == "]")):
                return False
    return len(stack) == 0


def main(filepath):
    """ Determine if the lines in a file contain balanced brackets.

    Args:
        filepath (str): path to a text file.
        
    Side effects:
        Writes to stdout.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if check_brackets(line):
                print(f"balanced: {line}")
            else:
                print(f"unbalanced: {line}")


def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a text file). The lines of the text file will
    be analyzed to see if they contain balanced brackets.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file to check for balanced brackets")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
