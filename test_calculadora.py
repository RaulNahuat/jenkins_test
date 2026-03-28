import pytest
from calculadora import sumar, restar, dividir

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(10, 5) == 5

def test_dividir_normal():
    assert dividir(10, 2) == 5.0

def test_dividir_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir entre cero"):
        dividir(10, 0)