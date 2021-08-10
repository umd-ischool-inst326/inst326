""" Test conversion of hours from 24-hour to 12-hour formats. """

# Replace "time_conversion" below with the name of your script (without the .py).
from time_conversion import convert_times

def test_convert_times_happy_path():
    """ Does convert_times() do the right thing for regular times? """
    assert convert_times([2]) == ["2 in the morning"]
    assert convert_times([15]) == ["3 in the afternoon"]
    assert convert_times([19]) == ["7 in the evening"]
    assert convert_times([22]) == ["10 at night"]

def test_convert_times_returns_list():
    """ Does convert_times() return a list of several values as expected? """
    assert convert_times([3, 5, 16]) == ["3 in the morning", "5 in the morning",
                                         "4 in the afternoon"]

def test_midnight():
    """ Does convert_times() correctly handle midnight? """
    assert convert_times([0]) == ["12 midnight"]

def test_noon():
    """ Does convert_times() correctly handle noon? """
    assert convert_times([12]) == ["12 noon"]
