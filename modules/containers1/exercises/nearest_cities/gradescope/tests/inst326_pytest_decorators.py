import pytest
import decorator


def pts(n):
    def deco(func):
        func.points = n
        def wrapper(func, *args, **kwargs):
            return func(*args, **kwargs)
        return decorator.decorator(wrapper, func)
    return deco


def num(n):
    def deco(func):
        func.number = n
        def wrapper(func, *args, **kwargs):
            return func(*args, **kwargs)
        return decorator.decorator(wrapper, func)
    return deco
