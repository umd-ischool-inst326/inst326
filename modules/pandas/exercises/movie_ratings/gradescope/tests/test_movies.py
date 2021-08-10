import pandas as pd
import pytest

from inst326_pytest_decorators import pts, num

from movies import best_movies as student_best


def best_movies(movie_csv, ratings_csv):
    """ Find the average rating of each movie. Results are sorted from highest
    rating to lowest.

    Args:
        movie_csv (str): a CSV file of movie information.
        ratings_csv (str): a CSV file of movie ratings.

    Returns:
        Series: the average ratings for each movie, sorted from highest rating
            to lowest. The index labels are movie titles; the values are floats.
    """
    df_movies = pd.read_csv(movie_csv)
    df_ratings = pd.read_csv(ratings_csv)
    df = (df_ratings.merge(df_movies, left_on="item id", right_on="movie id",
                           how="inner").drop("item id", axis=1))
    movies_by_rating = df.groupby("movie title")["rating"].mean()
    return movies_by_rating.sort_values(ascending=False)


@num("1.1")
@pts(4)
def test_best_movies():
    """Does the best_movies() function return the correct result?"""
    assert student_best("m.csv", "r.csv").equals(best_movies("m.csv", "r.csv"))

@num("2.1")
@pts(1)
def test_best_movies_docstring_exists():
    """Does best_movies() have a docstring?"""
    docstr = student_best.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "best_movies() has no docstring"

@num("2.2")
@pts(1)
def test_best_movies_docstring_contents():
    """Does best_movies() docstring have the correct sections?"""
    for section in ["Args:", "Returns:"]:
        assert section in student_best.__doc__, \
            f"best_movies() docstring has no '{section}' section"
