import builtins
from _pytest.fixtures import FixtureRequest
from pytest import fixture
from unittest import mock

from inst326_pytest_decorators import num, pts

from hangman import Player, HumanPlayer, ComputerPlayer, GameState, Game


class NaivePlayer(Player):
    def __init__(self, name, vocab):
        """Initialize the computer player.
        
        Args:
            name (str): the player's name.
            vocab (list of str): words the player knows.
        
        Side effects:
            Sets self.name and self.vocab.
        """
        super().__init__(name)
        self.vocab = vocab
    
    def turn(self, state):
        """Take a turn.
        
        Args:
            state (GameState): a snapshot of the current state of the game.
        
        Returns:
            str: the player's guess (a letter or a word).
        """
        unguessed = state.unguessed.copy()
        return unguessed.pop()


@fixture
def wordlist():
    return ['PINECONE', 'CROWN', 'SIDESTREAM', 'CONTEXT', 'SLAW', 'HYPOTHESIS',
            'TABLE', 'ALBATROSS', 'TOUCH', 'NETWORKING', 'SNOWMOBILING',
            'APPAREL', 'DIVAN', 'SEDIMENT', 'BUILDING', 'DESCENDANT', 'TURN',
            'CHILDHOOD', 'HAIRCUT', 'BEETLE', 'SPHYNX', 'DUTY', 'LAYER',
            'HABIT', 'BILLION', 'MISREADING', 'PAVILION', 'HUNT', 'MUSIC',
            'CREATOR', 'ANTELOPE', 'SEPARATION', 'MISSILE', 'WATERCRESS',
            'SPONGE', 'CRISIS', 'IDIOM', 'REHOSPITALISATION', 'PETTICOAT',
            'SPASM', 'LIVER', 'SHEEP', 'MORBIDITY', 'SAUERKRAUT', 'INFANT',
            'INSIGHT', 'SCOTCH', 'WOOL', 'COMBINE', 'YARD']


@fixture
def humanplayer():
    return HumanPlayer("human")


@fixture
def computerplayer(wordlist):
    return ComputerPlayer("computer", wordlist)

@num("1.1")
@pts(0.5)
def test_human_init(humanplayer):
    """Does HumanPlayer.__init__() do the right thing?"""
    assert humanplayer.name == "human", \
        "unexpected value for name attribute of HumanPlayer object"

@num("1.2")
@pts(1)
def test_human_turn(humanplayer, capsys, monkeypatch):
    """Does HumanPlayer.turn() do the right thing?"""
    monkeypatch.setattr(GameState, "__str__", lambda self: "CORRECT")
    state = GameState("aardvark", set(), set(), {}, 10)
    with mock.patch("builtins.input", side_effect=["x"]):
        result = humanplayer.turn(state)
        assert result == "x", "unexpected return value from HumanPlayer.turn()"
        captured = capsys.readouterr()
        assert captured.out == "CORRECT\n", \
            "HumanPlayer.turn() did not print the board correctly"
            
@num("2.1")
@pts(0.5)
def test_computer_init(computerplayer, wordlist):
    """Does ComputerPlayer.__init__() do the right thing?"""
    assert computerplayer.name == "computer", \
        "unexpected value for name attribute of ComputerPlayer object"
    assert computerplayer.vocab == wordlist, \
        "unexpected value for vocab attribute of ComputerPlayer object"

@num("2.2")
@pts(0.75)
def test_computer_turn(computerplayer):
    """Does ComputerPlayer.turn() do something sensible?"""
    state = GameState("context", set(), set(), {"computer": 0}, 10)
    result = computerplayer.turn(state)
    assert isinstance(result, str), "ComputerPlayer.turn() should return a string"
    assert len(result) in [1, 7], \
        "unexpected guess from ComputerPlayer.turn()"

@num("2.3")
@pts(0.75)
def test_computer2(computerplayer, wordlist, monkeypatch):
    """Can ComputerPlayer.turn() outperform a naive ComputerPlayer?"""
    def play(self):
        turn = -1
        player = None
        while self.outcome() is None:
            turn += 1
            player = self.players[turn % len(self.players)]
            if self.score[player.name] > self.max_bad_guesses:
                continue
            self.turn(player)
        print(self.state().board)
        outcome = self.outcome()
        if outcome == "win":
            print(f"{player.name} wins!")
            self.winner = player
        else:
            print(f"The word was {self.word}. Better luck next time.")
            self.winner = None
    
    monkeypatch.setattr(Game, "play", play)
    np = NaivePlayer("naive", wordlist)
    players = [np, computerplayer]
    score = {np: 0, computerplayer: 0}
    for i in range(100):
        computerplayer.vocab = wordlist[:]
        g = Game(wordlist, players)
        g.play()
        score[g.winner] = score.get(g.winner, 0) + 1
        players.reverse()
    assert score[computerplayer] >= score[np] * 1.25

@num("3.1")
@pts(0.25)
def test_humanplayer_docstring():
    """Does HumanPlayer class have a docstring?"""
    docstr = HumanPlayer.__doc__
    assert isinstance(docstr, str) and len(docstr.strip()) > 0, \
        "HumanPlayer class has no docstring"

@num("3.2")
@pts(0.25)
def test_humanplayer_docstring_contents():
    """Does HumanPlayer class docstring have the right elements?"""
    docstr = HumanPlayer.__doc__
    assert "Attributes:" in docstr, \
        "HumanPlayer docstring has no Attributes: section"

@num("3.3")
@pts(0.25)
def test_humanplayer_turn_docstring():
    """Does HumanPlayer.turn() method have a docstring?"""
    docstr = HumanPlayer.turn.__doc__
    assert isinstance(docstr, str) and len(docstr.strip()) > 0, \
        "HumanPlayer.turn() method has no docstring"

@num("3.4")
@pts(0.25)
def test_humanplayer_turn_docstring_contents():
    """Does HumanPlayer class docstring have the right elements?"""
    docstr = HumanPlayer.turn.__doc__
    assert "Args:" in docstr, \
        "HumanPlayer.turn() docstring has no Args: section"
    assert "Returns:" in docstr, \
        "HumanPlayer.turn() docstring has no Returns: section"
        

@num("4.1")
@pts(0.25)
def test_computerplayer_docstring():
    """Does ComputerPlayer class have a docstring?"""
    docstr = ComputerPlayer.__doc__
    assert isinstance(docstr, str) and len(docstr.strip()) > 0, \
        "ComputerPlayer class has no docstring"

@num("4.2")
@pts(0.25)
def test_computerplayer_docstring_contents():
    """Does ComputerPlayer class docstring have the right elements?"""
    docstr = ComputerPlayer.__doc__
    assert "Attributes:" in docstr, \
        "ComputerPlayer docstring has no Attributes: section"

@num("4.3")
@pts(0.25)
def test_computerplayer_turn_docstring():
    """Does ComputerPlayer.turn() method have a docstring?"""
    docstr = ComputerPlayer.turn.__doc__
    assert isinstance(docstr, str) and len(docstr.strip()) > 0, \
        "ComputerPlayer.turn() method has no docstring"

@num("4.4")
@pts(0.25)
def test_computerplayer_turn_docstring_contents():
    """Does ComputerPlayer class docstring have the right elements?"""
    docstr = ComputerPlayer.turn.__doc__
    assert "Args:" in docstr, \
        "ComputerPlayer.turn() docstring has no Args: section"
    assert "Returns:" in docstr, \
        "ComputerPlayer.turn() docstring has no Returns: section"
