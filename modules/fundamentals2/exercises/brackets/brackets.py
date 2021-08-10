from argparse import ArgumentParser
import sys


# Replace this comment with your implementation of check_brackets() and main().


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
