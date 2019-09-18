import pytest 
from principal import somar
from principal import subtrair

def test_somar():
    assert somar(2,4) == 6
    assert somar(4,4) != 0

def test_subtrair():
    assert subtrair(10,5) == 5
    assert subtrair(5,4) > 0