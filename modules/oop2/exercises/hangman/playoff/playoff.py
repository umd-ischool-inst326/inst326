from argparse import ArgumentParser
from collections import Counter
import importlib
import importlib.util
from pathlib import Path
import re
import sys
from time import sleep, time
from timeout_decorator import timeout
from timeout_decorator.timeout_decorator import TimeoutError

from hangman import Game


TIMEOUT_LIMIT = 0.5
ROUND1_LIMIT = 10
DEFAULT_GAMES_PER_MATCH = 101


class TurnError(Exception):
    def __init__(self, message="", player=None, error=None):
        super().__init__(self.message)
        self.player = player
        self.error = error


class PlayoffGame(Game):
    def play(self):
        turn = -1
        player = None
        while self.outcome() is None:
            turn += 1
            player = self.players[turn % len(self.players)]
            if self.score[player.name] > self.max_bad_guesses:
                continue
            try:
                timeout(TIMEOUT_LIMIT)(self.turn)(player)
            except Exception as e:
                raise TurnError(player=player, error=e)
        print(self.state().board)
        outcome = self.outcome()
        if outcome == "win":
            return player
        else:
            return None
            

class Playoff:
    def __init__(self, directories, wordlist1, wordlist2=None,
                 games_per_match=DEFAULT_GAMES_PER_MATCH, verbose=False):
        self.wordlist1 = wordlist1
        self.wordlist2 = wordlist2 if wordlist2 else wordlist1
        self.games_per_match = games_per_match
        self.verbose = verbose
        self.contestants = dict()
        self.eliminated = list()
        self.offset = 0
        for directory in directories:
            for path in directory.iterdir():
                if path.is_dir():
                    self.load_submission(path)

    def import_submission(self, path):
        try:
            spec = importlib.util.spec_from_file_location("submission", str(path.resolve()))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module.ComputerPlayer
        except Exception as e:
            if self.verbose:
                print("{str(path)} failed to import", file=sys.stderr)
            raise ImportError(path=path)

    @staticmethod
    def get_submission(directory):
        expected = directory / "hangman.py"
        if expected.exists():
            return expected
        for path in directory.glob("*.py"):
            contents = path.read_text(encoding="utf-8")
            if re.search(r"class\s+ComputerPlayer", contents):
                return path
        raise FileNotFoundError
        
    def assign_key(self, directory_path):
        key = directory_path.name
        if key in self.contestants:
            n = 1
            while True:
                n += 1 
                key2 = key + str(n)
                if key2 not in self.contestants:
                    return key2
        return key
    
    def load_submission(self, directory_path):
        try:
            submission = self.get_submission(directory_path)
        except FileNotFoundError:
            if self.verbose:
                print(f"No submission in {str(directory_path)}",
                        file=sys.stderr)
            return
        try:
            cls =  self.import_submission(submission)
        except ImportError:
            return
        key = self.assign_key(directory_path)
        self.contestants[key] = cls
    
    def match(self, name1, name2):
        score = {name1: 0, name2: 0}
        for i in range(self.games_per_match):
            p1 = self.contestants[name1](name1, self.wordlist2[:])
            p2 = self.contestants[name2](name1, self.wordlist2[:])
            if p1.name != name1:
                return name2
            if p2.name != name2:
                return name1
            g = PlayoffGame(self.wordlist1, [p1, p2])
            try:
                winner = g.play()
            except TurnError as e:
                winner = (set(score) - {e.player.name}).pop()
            if winner:
                score[winner.name] += 1
        if score[name1] == score[name2]:
            return None
        return max(score, key=score.get)
    
    def eliminate(self, name):
        self.contestants.pop(name)
        self.eliminated.append(name)
        print(f"{name} has been eliminated")
        sleep(0.5)

    def round(self, elimination=False):
        scores = Counter()
        self.offset += 1
        if self.offset % len(self.contestants) == 0:
            self.offset = 1
        names = list(self.contestants)
        names1 = names[:]
        names2 = names[self.offset:] + names[:self.offset]
        if elimination:
            names1 = names[:len(names)//2]
            names2 = names[len(names)//2:]
        for name1, name2 in zip(names1, names2):
            if name1 not in self.contestants or name2 not in self.contestants:
                continue
            winner = self.match(name1, name2)
            print(name1, name2, winner)
            if winner:
                scores[winner] = 1
                if elimination:
                    self.eliminate(({name1, name2} - {winner}).pop())
        return scores
    
    def playoff(self):
        t = time()
        round_count = 0
        scores = Counter()
        seen = set()
        while True:
            round_count += 1
            scores += self.round()
            if round_count == len(self.contestants) - 1 or time() - t >= ROUND1_LIMIT:
                break
        for name in set(self.contestants) - set(scores):
            self.eliminate(name)
        while len(self.contestants) > 1:
            contestants = frozenset(self.contestants)
            if contestants in seen:
                break
            seen.add(contestants)
            self.round(elimination=True)
        winners = list(self.contestants)
        for w in winners:
            print(f"{w} wins!")


def read_words(path):
    return [w.upper() for w in path.read_text(encoding="utf-8").splitlines()
            if w.strip()]


def main(directories, wordfile1, wordfile2=None,
         games_per_match=DEFAULT_GAMES_PER_MATCH, verbose=False):
    wordlist1 = read_words(wordfile1)
    wordlist2 = read_words(wordfile2) if wordfile2 else None
    p = Playoff(directories, wordlist1, wordlist2=wordlist2,
                games_per_match=games_per_match, verbose=verbose)
    p.playoff()


def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("dirs", type=Path, nargs="+",
                        help="directories containing submissions (each"
                        " submission is its own directory)")
    parser.add_argument("wordlist", type=Path, help="wordlist for game")
    parser.add_argument("-t", "--vocablist", type=Path, help="vocabulary for"
                        " players")
    parser.add_argument("-g", "--games_per_match", type=int,
                        default=DEFAULT_GAMES_PER_MATCH,
                        help="games per match")
    parser.add_argument("-v", "--verbose", help="verbose")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.dirs, args.wordlist, wordfile2=args.vocablist,
         games_per_match=args.games_per_match, verbose=args.verbose)
