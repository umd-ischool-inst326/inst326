from rpn import evaluate
from pytest import approx

def test_evaluate_edge_cases():
    """ Unusual but correct test cases for the evaluate() function. """
    assert evaluate("5") == approx(5)
    assert evaluate("2.3") == approx(2.3)
    assert evaluate("-2") == approx(-2)
    assert evaluate("42") == approx(42)
    
def test_evaluate_happy_path_cases():
    """ Typical test cases for the evaluate() function. """
    assert evaluate("5 3 +") == approx(8)
    assert evaluate("5 3 -") == approx(2)
    assert evaluate("5 3 *") == approx(15)
    assert evaluate("5 3 /") == approx(1.66666666667)
    assert evaluate("4 3 7 * -") == approx(-17)
    assert evaluate("5 2 / 4 +") == approx(6.5)
