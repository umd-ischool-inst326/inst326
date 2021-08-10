""" Convert words to a "value" based on the sum of the values of their
letters where a=1, b=2, .. z=26. """


from argparse import ArgumentParser
import sys


class WordValue:
    """ Convert words to "values" based on the sum of the values of
    their letters where a=1, b=2, .. z=26.
    
    Attributes:
        words (dict of str: int): a mapping of words to their values.
    """
    def __init__(self, filename):
        """ Read words from filename and build a dictionary of words
        and values.
        
        Args:
            filename (str): path to a file consisting of one word per
                line.
        
        Side effects:
            Creates attribute words.
        """
        with open(filename, "r", encoding="utf-8") as f:
            self.words = {w.strip(): self.appraise_word(w) for w in f}
        
    def appraise_word(self, w):
        """ Determine the "value" of a word by summing the values of
        its letters.
        
        Args:
            w (str): the word whose value should be calculated.
        
        Returns:
            int: the value of the word.
        """
        return sum(ord(c) - ord("a") + 1 for c in w.lower()
                   if ord("a") <= ord(c) <= ord("z"))
    
    def words_by_value(self, v):
        """ Return all words that have a value v.
        
        Args:
            v (int): the target value.
        
        Returns:
            list of str: the words whose value is v.
        """
        return [w for w in self.words if self.words[w] == v]
 

def main(filename, target_value=None, interactive=False):
    """ Determine values of words from a file and print words with a
    specified value.
    
    This function has two modes: interactive and batch
    (non-interactive). In batch mode, words matching target_value will
    be printed to stdout. In interactive mode, the function will ask the
    user for values and print the words corresponding to those values.
    
    Args:
        filename (str): the name of a file containing one word per line.
        target_value (int): the value of words to print out. Ignored if
            interactive is True.
        interactive (bool): if True, run the function in interactive
            mode; otherwise, run in batch mode (see description above).
    
    Side effects:
        Writes to stdout.
    """
    if not interactive and target_value is None:
        raise ValueError("must specify target value in batch mode")
    wv = WordValue(filename)
    if interactive:
        # interactive mode
        while True:
            response = input("Enter a word value (or q to quit): ")
            response = response.strip().lower()
            if response == "q":
                return
            try:
                value = int(response)
                print("\n".join(wv.words_by_value(value)))
            except ValueError:
                print("value must be an integer")
            print()
    else:
        # batch mode
        print("\n".join(wv.words_by_value(target_value)))
    

def parse_args(arglist):
    """ Parse command line arguments.
    
    The user must specify a filename. The user must also decide whether
    to run the program in batch mode (in which case the user should
    specify a value with the -v option) or in interactive mode (in which
    case the user should specify the -i option).
    
    Args:
        arglist (list of str): command-line arguments to parse.
    
    Returns:
        namespace: the parsed arguments as a namespace with variables
        filename, value, and interactive.
    """
    parser = ArgumentParser()
    parser.add_argument("filename", help="file containing one word per line")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-v", "--value", type=int,
                       help="find words with this value")
    group.add_argument("-i", "--interactive", action="store_true",
                       help="enter values interactively")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename, args.value, args.interactive)
