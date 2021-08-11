""" Unit-test the main function from the bulk pricing script. """


from bulk_pricing_solution import get_cost


def test_get_cost_happy_path():
    assert get_cost(1) == 0.75
    assert get_cost(25) == 25 * 0.75
    assert get_cost(75) == 75 * 0.72
    assert get_cost(200) == 200 * 0.7
    assert get_cost(1200) == 1200 * 0.67
        
    
def test_get_cost_edge_cases():
    assert get_cost(0) == 0
    assert get_cost(49) == 49*0.75
    assert get_cost(50) == 50*0.72
    assert get_cost(99) == 99*0.72
    assert get_cost(100) == 100*0.7
    assert get_cost(999) == 999*0.7
    assert get_cost(1000) == 1000*0.67
