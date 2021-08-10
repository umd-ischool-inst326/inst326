from argparse import ArgumentParser
import pandas as pd
import sys


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


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: the parsed command-line arguments as a namespace with
        variables movie_csv and rating_csv.
    """
    parser = ArgumentParser()
    parser.add_argument("movie_csv", help="CSV containing movie data")
    parser.add_argument("rating_csv", help="CSV containing ratings")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    movies = best_movies(args.movie_csv, args.rating_csv)
    print(movies.head())
