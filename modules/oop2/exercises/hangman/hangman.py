"""A hangman game that can be played by one or more players."""

from argparse import ArgumentParser
from random import choice
import re
import sys


MIN_WORD_LEN = 5
MAX_BAD_GUESSES = 6


class GameState:
    """Provide information on the current state of the game. Used in the
    Player.turn() method.
    
    Attributes:
        board (str): a representation of the board, with unguessed letters
            represented as dots ("\u2022").
        expr (str): a regular expression that matches the current board.
        guesses (set of str): characters that have already been guessed.
        bad_guesses (set of str): already-guessed characters that are not in
            the word.
        good_guesses (set of str): already-guessed characters that are in the
            word.
        blank_count (int): number of unguessed characters in the word.
        unguessed (set of str): characters that have not been guessed yet.
        guessed_words (set of str): words that have been guessed.
        score (dict of str: int): number of bad guesses made by each player;
            each key is a player's name.
        max_score (int): the maximum number of allowable bad guesses.
    """
    def __init__(self, word, guesses, guessed_words, score, max_score):
        """Set attributes."""
        def char_or_mask(char, mask, func=None):
            """Return the character or a mask character, depending on whether
            the character has already been guessed.
            
            Args:
                char (str): a character.
                mask (str): a mask to use for unguessed characters.
                func (function): if not None, apply this function to unmasked
                    characters.
            
            Returns:
                str: the unmasked character or the mask character.
            """
            if char in guesses or not char.isalpha():
                return func(char) if func else char
            return mask

        self.board = " ".join(char_or_mask(c, "\u2022") for c in word)
        self.expr = ("^"
                     + "".join(char_or_mask(c, ".", re.escape) for c in word)
                     + "$")
        self.guesses = guesses.copy()
        self.bad_guesses = guesses - set(word)
        self.good_guesses = guesses & set(word)
        self.blank_count = self.board.count("\u2022")
        self.unguessed = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ") - guesses
        self.guessed_words = guessed_words
        self.score = score.copy()
        self.max_score = max_score
    
    def __str__(self):
        """Return a string representation of the board."""
        result = [self.board,
                  f"Bad guesses: {sorted(self.bad_guesses)}"]
        for name, score in self.score.items():
            msg = f"{name} has made {score} of {self.max_score} bad guesses"
            result.append(msg)
        return "\n".join(result)
    
    def match(self, s):
        """Indicate whether s is compatible with the letters and blanks on the
        board. Returns a boolean."""
        return bool(re.search(self.expr, s.strip()))
    

class Game:
    """A hangman game.
    
    Attributes:
        players (list of Player): the players.
        score (dict of str: int): number of bad guesses made by each player;
            each key is a player's name.
        word (str): the word to be guessed.
        guesses (set of str): letters that have been guessed.
        max_bad_guesses (int): the maximum number of bad guesses a player can
            make; once they reach this limit, they lose.
    """
    def __init__(self, words, players):
        """Set attributes.
        
        Args:
            words (list of str): words to choose from.
            players (list of Player): the players.
        
        Side effects:
            Sets attributes.
            
        Raises:
            ValueError: players is not a list of Player objects, or two or more
                players have the same name.
        """
        if not all(isinstance(p, Player) for p in players):
            raise ValueError("players must be a list of Player objects")
        if len({p.name for p in players}) < len(players):
            raise ValueError("no two players may have the same name")
        self.players = players
        self.score = {p.name: 0 for p in players}
        self.word = choice(words).upper()
        self.guesses = set()
        self.guessed_words = set()
        self.max_bad_guesses = MAX_BAD_GUESSES // len(players) + 1
    
    def state(self):
        """Return the current state of the game as a GameState object."""
        return GameState(self.word, self.guesses, self.guessed_words,
                         self.score, self.max_bad_guesses)
    
    def turn(self, player):
        """Manage player's turn.

        Args:
            player (Player): the player whose turn it is.
        
        Side effects:
            Writes to stdout.
            May modify self.score, self.guessed_words, and/or self.guesses.
        """
        state = self.state()
        while True:
            guess = player.turn(state).strip().upper()
            if len(guess) == 0:
                continue
            elif len(guess) > 1:
                # player attempted to solve
                if guess == self.word:
                    self.guesses |= set(self.word)
                    print(f"{player.name} solved the puzzle!")
                else:
                    print(f"Sorry, {player.name}, the word is not '{guess}'.")
                    self.guessed_words.add(guess)
                    self.score[player.name] += 1
                return
            elif guess in self.guesses:
                print(f"{guess} has already been guessed.")
            elif not guess.isalpha():
                print(f"{guess} is not a letter.")
            else:
                # player made a valid one-letter guess
                self.guesses.add(guess)
                if guess not in self.word:
                    print(f"Sorry, {player.name}, there is no {guess} in the"
                          " word.")
                    self.score[player.name] += 1
                else:
                    count = self.word.count(guess)
                    verb, plural = ("is", "") if count == 1 else ("are", "s")
                    print(f"There {verb} {count} {guess}{plural} in the word!")
                return
    
    def outcome(self):
        """Determine if the game is over.
        
        Returns:
            "win" if a player has won, "loss" if all players have lost, or None
            if the game is not over.
        """
        if len(set(self.word) - self.guesses) == 0:
            return "win"
        elif all(v >= self.max_bad_guesses for v in self.score.values()):
            return "loss"
        else:
            return None
            
    def play(self):
        """Play hangman.
        
        Side effects:
            Writes to stdout.
            See also turn().
        """
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
        else:
            print(f"The word was {self.word}. Better luck next time.")


class Player:
    """Abstract base class for a hangman player.
    
    Attributes:
        name (str): the player's name.
    """
    def __init__(self, name):
        self.name = name
    
    def turn(self, state):
        """Take a turn.
        
        Args:
            state (GameState): a snapshot of the current state of the game.
        
        Returns:
            str: the player's guess (a letter or a word).
        """
        raise NotImplementedError


# Replace this comment with your implementation of the HumanPlayer and
# ComputerPlayer classes.


def main(wordlist, human_players, computer_player=False, computer_vocab=None):
    """Set up and play a game of hangman.

    Args:
        wordlist (str): path to a text file containing one word per line. Will
            be used to select a word for the game.
        human_players (list of str): names of the human players, if any.
        computer_player (bool, optional): if True, a computer player will be
            created. Defaults to False.
        computer_vocab (list of str, optional): a list of words that the
            computer player "knows". If None, wordlist will be used. Defaults
            to None.
    
    Side effects:
        Writes to stdout (see Game.play()).
    """
    with open(wordlist, "r", encoding="utf-8") as f:
        words = [line.strip().upper() for line in f
                 if len(line.strip()) >= MIN_WORD_LEN]
    players = [HumanPlayer(name) for name in human_players]
    if computer_player:
        if computer_vocab is not None:
            with open(computer_vocab, "r", encoding="utf-8") as f:
                vocab = [line.strip().upper() for line in f]
        else:
            vocab = words[:]
        players.append(ComputerPlayer("Computer", vocab))
    game = Game(words, players)
    game.play()


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect two mandatory arguments:
        - wordlist: a path to a file containing one word per line
        - names: one or more names of human players
    
    Also allow two optional arguments:
        -c, --computer_player: if specified, include a computer player.
        -v, --computer_vocab: if specified, it should be a path to another
            wordlist file for the computer to use as its vocab.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("wordlist", help="path to word list text file")
    parser.add_argument("names", nargs="*", help="player names")
    parser.add_argument("-c", "--computer_player", action="store_true",
                        help="add a computer player")
    parser.add_argument("-v", "--computer_vocab", help="path to word list for"
                        " computer")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.wordlist, args.names, args.computer_player, args.computer_vocab)
