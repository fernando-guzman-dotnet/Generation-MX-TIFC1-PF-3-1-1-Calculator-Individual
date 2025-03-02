import pytest
from main import sumar, restar, multiplicar, dividir, modulo

def test_sumar():
    assert sumar(2, 3, 5) == 10

def test_restar():
    assert restar(10, 4, 1) == 5

def test_multiplicar():
    assert multiplicar(2, 3, 4) == 24

def test_dividir():
    assert dividir(100, 5, 2) == 10

def test_modulo():
    assert modulo(100, 7, 3) == 2
