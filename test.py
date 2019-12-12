import pytest


def celcius(K):
    return round(int(K)-273.15 )
def fahrenheit(K):
    return round((int((K)-273.15) * 9/5 + 32))

def test_celcius():
    assert 27 == celcius(300)
def test_fahrenheit():
    assert 79 == fahrenheit(300)
