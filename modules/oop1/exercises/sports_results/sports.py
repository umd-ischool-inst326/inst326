class Match:
    """ Results of a match between Maryland and another collegiate team.
    
    Attributes:
        date (str): the date of the match.
        opponent (str): the other team.
        home (bool): if True, the game was hosted by Maryland.
        md_score (int): Maryland's final score.
        other_score (int): the other team's final score.
    """
    def __init__(self, date, opponent, home, md_score, other_score):
        """ Initialize attributes. """
        self.date = date
        self.opponent = opponent
        self.home = home
        self.md_score = md_score
        self.other_score = other_score
    
    def win(self):
        """ Determine if Maryland won the match. """
        return self.md_score > self.other_score


def read_scores(filename):
    """ Read scores from a file, as specified in the assignment.
    
    Args:
        filename (str): path to the file to be read in.
    
    Returns:
        list of Match: the results from the file as Match objects.
    """
    matches = list()
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            values = line.strip().split("|")
            date = values[0]
            home = values[1] == "home"
            opponent = values[2]
            md_score = int(values[3])
            other_score = int(values[4])
            matches.append(Match(date, opponent, home, md_score,
                                 other_score))
    return matches
