#!/usr/bin/env python3

"""
This program is designed to be run against an unpacked download of all the
submissions for the COVID assignment. You can copy check_covid.py into the
unpacked submission directory and run it with the username, for example:

    ./check_covid.py edsu

It will locate the user's submitted .py file, import it, and run the tests, and
let you examine the docstrings.
"""

import sys
import pytest
import pathlib
import inspect
import colorama
import importlib

CovidTestResult = None

def main():
    colorama.init()
    username = sys.argv[1]
    load_submission(sys.argv[1])
    run_tests()
    print_docstrings()

def load_submission(username):
    global CovidTestResult

    module_name = get_module(username)
    if module_name is None:
        exit(error(f'unable to find module for {username}'))
    try:
        submission = importlib.import_module(module_name)
    except Exception as e:
        exit(error(f'{module_name} does not compile: {e}'))

    if not hasattr(submission, 'CovidTestResult'):
        exit(error(f'{module_name} missing CovidTestResult class'))

    print()
    print(ok(f'loaded module {module_name} PASS'))
    CovidTestResult = submission.CovidTestResult

def get_module(username):
    for f in pathlib.Path('.').iterdir():
        if username in f.name:
            return f.name.replace('.py', '')
    return None

def run_tests():
    """Run tests in the current module."""
    for name, obj in inspect.getmembers(sys.modules['__main__']):
        if inspect.isfunction(obj) and name.startswith('test_'):
            try:
                obj.__call__()
                print(ok(f'{name} PASS'))
            except AssertionError as e:
                print(error(f'{name} FAIL - {e}'))

def ok(s):
    return colorama.Fore.GREEN + s + colorama.Style.RESET_ALL

def error(s):
    return colorama.Fore.RED + s + colorama.Style.RESET_ALL

def strong(s):
    return colorama.Style.BRIGHT + s + colorama.Style.RESET_ALL

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

def test_class_docstring():
    assert hasattr(CovidTestResult, '__doc__')
    assert CovidTestResult.__doc__ is not None

def test_method_docstrings():
    for name, obj in inspect.getmembers(CovidTestResult):
        if inspect.isfunction(obj):
            assert hasattr(obj, '__doc__')
            assert obj.__doc__ is not None

def print_docstrings():
    print()
    print('Here are the docstrings in CovidTestResult to check:')
    print()

    print(strong('CovidTestResult'))
    print(CovidTestResult.__doc__)

    for name, obj in inspect.getmembers(CovidTestResult):
        if inspect.isfunction(obj):
            doc = getattr(obj, '__doc__') or 'None'
            print()
            print(strong(name.strip()))
            print(doc.strip())
    print()

if __name__ == "__main__":
    main()
