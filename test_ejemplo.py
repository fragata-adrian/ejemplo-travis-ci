from ejemplo import *

def test_sumar():
    assert sumar(15, 5) == 20

def test_restar():
    assert restar(20, 5) == 15

def test_multiplicar():
    assert multiplicar(5, 5) == 25

def test_dividir():
    assert dividir(5, 2) == 2.5

def test_dividirSinResto():
    assert dividirSinResto(5, 2) == 2
