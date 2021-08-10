from itertools import product
import pandas as pd
import pytest
from random import randint
import time

from inst326_pytest_decorators import pts, num

import expectancy as exp


class Mock:
    def __init__(self):
        self.calls = []
    
    def call(self, *args, **kwargs):
        self.calls.append((args, kwargs, time.time()))


@pytest.fixture
def pletest(monkeypatch):
    mock1 = Mock()
    mock2 = Mock()
    monkeypatch.setattr(exp.sns, "jointplot", mock1.call)
    monkeypatch.setattr(exp.plt, "show", mock2.call)
    exp.plot_life_expectancy("lexp.csv", "Measles")
    return mock1, mock2


@num("1.1")
@pts(2)
def test_ple_plot(pletest):
    """Does plot_life_expectancy() call the jointplot() function correctly?"""
    mock1 = pletest[0]
    assert len(mock1.calls) > 0, "did not call sns.jointplot()"
    assert len(mock1.calls) == 1, "too many calls to sns.jointplot()"
    args, kwargs, time = mock1.calls[0]
    assert len(args) == 0, f"unexpected arguments to sns.jointplot(): {args}"
    for arg in ["data", "x", "y", "hue"]:
        assert "data" in kwargs, f"call to sns.joinplot() is missing {arg} argument"
    assert isinstance(kwargs["data"], pd.DataFrame), \
        "data argument to sns.jointplot() should be a DataFrame"
    assert len(kwargs["data"]["Year"].unique()) == 1, \
        "DataFrame is not filtered by year"
    assert 2015 in list(kwargs["data"]["Year"]), \
        "DataFrame should only contain data from 2015"
    assert kwargs["x"] == "Life expectancy", \
        "unexpected value for x parameter of sns.jointplot()"
    assert kwargs["y"] == "Measles", \
        "unexpected value for y parameter of sns.jointplot()"
    assert kwargs["hue"] == "Status", \
        "unexpected value for hue parameter of sns.jointplot()"


@num("1.2")
@pts(2)
def test_ple_showplot(pletest):
    """Does plot_life_expectancy() show the plot?"""
    mock2 = pletest[1]
    assert len(mock2.calls) > 0, "did not call plt.show()"
    assert len(mock2.calls) == 1, "too many calls to plt.show()"
    assert mock2.calls[0][-1] > pletest[0].calls[0][-1], \
        "called plt.show() before creating plot"


@num("2.1")
@pts(1)
def test_ple_docstring_exists():
    """Does plot_life_expectancy() have a docstring?"""
    docstr = exp.plot_life_expectancy.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "plot_life_expectancy() has no class docstring"


@num("2.2")
@pts(1)
def test_ple_docstring_contents():
    """Does plot_life_expectancy() docstring have the correct sections?"""
    for section in ["Args:"]:
        assert section in exp.plot_life_expectancy.__doc__, \
            f"plot_life_expectancy() docstring has no '{section}' section"
