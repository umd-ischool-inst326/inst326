def rpsfw(item1, item2):
    """ Determine the winner of a game of rock, paper, scissors, fire, water.
    
    Args:
        item1 (str): one of the following strings: "rock", "paper", "scissors",
            "fire", or "water".
        item2 (str): another of the five strings mentioned above. May or may not
            be identical to item1.
    
    Returns:
        int: 0 if a tie, 1 if item1 defeats item2, or 2 if item2 defeats item1.
    """
    tie = item1 == item2
    item1_wins = (item1 == "water" and item2 == "fire"
                  or item1 == "fire" and item2 != "water"
                  or item1 == "paper" and item2 in ["rock", "water"]
                  or item1 == "rock" and item2 in ["paper", "water"]
                  or item1 == "scissors" and item2 in ["rock", "water"])
    return 0 if tie else 1 if item1_wins else 2
