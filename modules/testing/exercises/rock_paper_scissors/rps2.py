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
    if item1 == item2:
        return 0
    if (item1 == "paper" and item2 == "rock"
        or item1 == "scissors" and item2 == "paper"
        or item1 == "rock"):
        return 1
    return 2
