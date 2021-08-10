from rpn import evaluate
from math import isclose

def test_evaluate_edge_cases():
    """ Unusual but correct test cases for the evaluate() function. """
    assert isclose(evaluate("5"), 5)
    assert isclose(evaluate("2.3"), 2.3)
    assert isclose(evaluate("-2"), -2)
    assert isclose(evaluate("42"), 42)
    
def test_evaluate_happy_path_cases():
    """ Typical test cases for the evaluate() function. """
    assert isclose(evaluate("5 3 +"), 8)
    assert isclose(evaluate("5 3 -"), 2)
    assert isclose(evaluate("5 3 *"), 15)
    assert isclose(evaluate("5 3 /"), 1.66666666667)
    assert isclose(evaluate("4 3 7 * -"), -17)
    assert isclose(evaluate("5 2 / 4 +"), 6.5)
