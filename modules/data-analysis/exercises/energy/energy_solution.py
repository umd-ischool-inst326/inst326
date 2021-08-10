""" Build a database of energy sources in the US. """


from argparse import ArgumentParser
import sqlite3
import sys


class EnergyDB:
    """ A database of energy sources in the US.
    
    Attributes:
        conn (sqlite3.Connection): connection to an in-memory sqlite database
    """
    def __init__(self, filename):
        """ Create and populate an in-memory database using data from
        filename. """
        self.conn = sqlite3.connect(":memory:")
        self.read(filename)
        
    def __del__(self):
        """ Clean up the database connection. """
        try:
            self.conn.close()
        except:
            pass
        
    def read(self, filename):
        """ Populate the database using data from filename.
        
        Args:
            filename (str): path to a CSV file containing four columns:
                Year, State, Energy Source, Megawatthours.
        
        Side effects:
            Creates and populates a table in the database with the following
            columns: year (int), state (str), source (str), mwh (float).
        """
        c = self.conn.cursor()
        c.execute("""CREATE TABLE production
                     (year integer, state text, source text, mwh real)""")
        with open(filename, "r", encoding="utf-8") as f:
            f.readline()
            data = list()
            for line in f:
                yrstr, state, src, mwhstr = line.split(",")
                year = int(yrstr)
                mwh = float(mwhstr)
                data.append((year, state, src, mwh))
        c.executemany("INSERT INTO production VALUES (?,?,?,?)", data)
        self.conn.commit()
        
    def production_by_source(self, source, year):
        """ Find the total energy production in megawatt-hours of all energy
        from the specified source in a specified year.
        
        Args:
            source (str): a source of energy from the CSV file (e.g., "Wind").
            year (int): a year represented in the CSV file.
        
        Returns:
            float: the total energy production for the source and year
            specified by the user.
        """
        c = self.conn.cursor()
        cmd = "SELECT mwh FROM production WHERE source=? AND year=?"
        c.execute(cmd, (source, year))
        return sum(tup[0] for tup in c.fetchall())


def main(filename):
    """ Build a database of energy sources and calculate the total production
    of solar and wind energy.
    
    Args:
        filename (str): path to a CSV file containing four columns:
            Year, State, Energy Source, Megawatthours.
    
    Side effects:
        Writes to stdout.
    """
    e = EnergyDB(filename)
    sources = [("solar", "Solar Thermal and Photovoltaic"),
               ("wind", "Wind")]
    for source_lbl, source_str in sources:
       print(f"Total {source_lbl} production in 2017: ",
             e.production_by_source(source_str, 2017))


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file", help="path to energy CSV file")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
