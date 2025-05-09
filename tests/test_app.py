# tests/test_app.py
from src.app import (add_numbers,multiplication_numbers,soustraction_numbers, division_numbers, int_divide_numbers,modulo_numbers)
from src.app import *

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(10,20) == 30

def test_multiplication_numbers():
    assert multiplication_numbers(2, 3) == 6
    assert multiplication_numbers(-1, 1) == -1
    assert multiplication_numbers(10,20) == 200

def test_soustraction_numbers():
    assert soustraction_numbers(2, 3) == -1
    assert soustraction_numbers(-1, 1) == -2
    assert soustraction_numbers(10,20) == -10 #erreur de test


def test_division_numbers():
    assert division_numbers(3, 2) == 1.5
    assert division_numbers(-1, 1) == -1
    assert division_numbers(10,20) == 0.5


def test_int_divide_numbers():
    assert int_divide_numbers(3, 2) == 1
    assert int_divide_numbers(11, 10) == 1
    assert int_divide_numbers(20,7) == 2

def test_modulo_numbers():
    assert modulo_numbers(3, 2) == 1
    assert modulo_numbers(11, 3) == 2
    assert modulo_numbers(10,20) == 10