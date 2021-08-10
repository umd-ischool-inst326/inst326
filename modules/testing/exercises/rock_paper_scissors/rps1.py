def rps(item1, item2):
    """ Determine the winner of a game of rock, paper, scissors.
    
    Args:
        item1 (str): one of the following strings: "rock", "paper", or
            "scissors".
        item2 (str): another of the three strings mentioned above. May or may
            not be identical to item1.
    
    Returns:
        int: 0 if a tie, 1 if item1 defeats item2, or 2 if item2 defeats item1.
    """
    values = ["rock", "paper", "scissors"]
    n1 = values.index(item1)
    n2 = values.index(item2)
    return (n1 - n2) % 3
