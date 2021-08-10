from covid import CovidTestResult

def test_valid():
    c = CovidTestResult(.96, 3)
    assert c.is_valid(), "test result is valid"

def test_invalid_sample():
    c = CovidTestResult(.91, 3)
    assert not c.is_valid(), "sample is invalid"

def test_invalid_calibration():
    c = CovidTestResult(.96, 8)
    assert not c.is_valid(), "calibration is invalid"

def test_all_invalid():
    c = CovidTestResult(.8, 10)
    assert not c.is_valid(), "sample and calibration are invalid"
