from covid import Vaccinations

def test_constructor():
    v = Vaccinations()

def test_read_csv():
    v = Vaccinations()
    v.read_csv('covid-vaccinations.csv')

def test_total_records():
    v = Vaccinations()
    v.read_csv('covid-vaccinations.csv')
    assert v.total_records() >= 672 


