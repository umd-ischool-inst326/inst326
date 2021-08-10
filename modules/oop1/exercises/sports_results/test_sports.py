# change sports in the following line to the name of your module

from sports import Match, read_scores
from pathlib import Path

def test_match1():
    """ Test the Match class. Part 1 of 2. """
    date, opponent, home, md_score, other_score = (
        "03/04/18", "Georgetown", True, 6, 8
    )
    m = Match(date, opponent, home, md_score, other_score)
    assert m.date == date
    assert m.opponent == opponent
    assert m.home == home
    assert m.md_score == md_score
    assert m.other_score == other_score
    assert not m.win()

def test_match2():
    """ Test the Match class. Part 2 of 2. """
    date, opponent, home, md_score, other_score = (
        "03/04/18", "American University", False, 10, 3
    )
    m = Match(date, opponent, home, md_score, other_score)
    assert m.date == date
    assert m.opponent == opponent
    assert m.home == home
    assert m.md_score == md_score
    assert m.other_score == other_score
    assert m.win()

def test_read_scores():
    """ Test the read_scores() function.
    
    Side effects:
        Creates and deletes a temporary file in the current working
        directory.
    """
    sample_data = """03/03/19|away|Notre Dame|13|14
03/09/19|home|Albany (NY)|14|9
"""
    filename = "TEMPORARY_TEST_FILE.txt"
    try:
        # create temporary file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(sample_data)
        
        # read temporary file
        result = read_scores(filename)
        
        # check length of result
        assert len(result) == 2, \
            "read_scores() returns an unexpected number of results"
        
        # check types of data in result
        for item in result:
            assert isinstance(item, Match), \
                ("values in return value of read_scores() should be"
                " instances of Match class")
        
        # check values of specific attributes
        assert result[0].date == "03/03/19"
        assert result[0].opponent == "Notre Dame"
        assert result[0].home == False
        assert result[0].md_score == 13
        assert result[0].other_score == 14
        
        assert result[1].date == "03/09/19"
        assert result[1].opponent == "Albany (NY)"
        assert result[1].home == True
        assert result[1].md_score == 14
        assert result[1].other_score == 9
    finally:
        # attempt to clean up the temporary file
        try:
            Path(filename).unlink()
        except:
            pass
