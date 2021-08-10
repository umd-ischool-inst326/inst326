import re


def get_words(s):
    """ Extract a list of words from string s.

    Args:
        s (str): a string containing one or more words.

    Returns:
        list of str: a list of words from s converted to lower-case.
    """
    words = list()
    s = re.sub(r"--+", " ", s)
    for word in re.findall(r"[\w'-]+", s):
        word = word.strip("'-_")
        if len(word) > 0:
            words.append(word.lower())
    return words


class UniqueWords:
    """ A class to identify words that are unique to specific texts.
    
    Attributes:
        all_words (set of str): all the words encountered in all the
            texts.
        unique_words (set of str): words that appear in only one text.
        words_by_file (dict of str: set of str): all the words that
            appear in each file.
    """
    def __init__(self):
        self.all_words = set()
        self.unique_words = set()
        self.words_by_file = dict()
    
    def add_file(self, filename, key):
        """ Read a file and update the set of unique words.
        
        Args:
            filename (str): the path to a file to be read in.
            key (str): a nickname for the file to be read in.
        
        Side effects:
            Updates attributes all_words, unique_words, and
            words_by_file.
        """
        # read the file and get the set of words it contains
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
            self.words_by_file[key] = set(get_words(text))
            
        # remove any previously unique words that appear in the new file
        self.unique_words -= self.words_by_file[key]
        
        # find words that are unique to this file
        new_words = self.words_by_file[key] - self.all_words
        
        # update unique_words to contain the words unique to this file
        self.unique_words |= new_words
        
        # update all_words to contain the new words from this file
        self.all_words |= new_words
    
    def unique(self, key):
        """ Get the set of words that are unique to the file represented
        by key.
        
        Args:
            key (str): a key in self.words_by_file, representing one of
                the files that have been read in.
        
        Returns:
            set of str: the words that are unique to the requested file.
        """
        return self.unique_words & self.words_by_file[key]
