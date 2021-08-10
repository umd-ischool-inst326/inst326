from argparse import ArgumentParser
from pathlib import Path
import sys

# change unique_words below to the name of your script
from unique_words import UniqueWords


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): arguments received from the command line.
    
    Returns:
        namespace: a namespace with one variable, files, a list of files
        to read in.
    """
    parser = ArgumentParser()
    parser.add_argument("files", nargs="+", help="files to analyze")
    args = parser.parse_args(arglist)
    return args


def main(files):
    """ Read files and print out lists of unique words from those files.
    
    Args:
        files (list of str): a list of paths to files to be read in.
    
    Side effects:
        Writes to stdout.
    """

    uw = UniqueWords()
    for filename in files:
        # use the "stem" of the file as a key
        # (the stem is the filename without directory or file extension)
        uw.add_file(filename, Path(filename).stem)
    for key in uw.words_by_file:
        print(f"Words only found in {key}:")
        print("\n".join(uw.unique(key)))
        print()
        

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.files)
