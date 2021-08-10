from rps1 import rps


def test_rps():
    """ Test all possible outcomes of rock, paper, scissors. """
    assert rps("rock", "rock") == 0
    assert rps("rock", "paper") == 2
    assert rps("rock", "scissors") == 1
    assert rps("paper", "paper") == 0
    assert rps("paper", "scissors") == 2
    assert rps("paper", "rock") == 1
    assert rps("scissors", "scissors") == 0
    assert rps("scissors", "rock") == 2
    assert rps("scissors", "paper") == 1
