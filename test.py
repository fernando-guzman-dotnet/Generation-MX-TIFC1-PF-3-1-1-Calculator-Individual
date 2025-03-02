import pytest
from main import sumar, restar, multiplicar, dividir, modulo

def test_sumar():
    assert sumar(5, 3) == 8

def test_restar():
    assert restar(10, 4) == 6

def test_multiplicar():
    assert multiplicar(6, 7) == 42

def test_dividir():
    assert dividir(9, 3) == 3

def test_modulo():
    assert modulo(10, 3) == 1
