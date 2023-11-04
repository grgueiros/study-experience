from pytest import mark
from soma_hipotenusas import eh_hipotenusa, soma_hipotenusas

@mark.parametrize('entrada, expected', [(5, True), (10, True), (11, False)])
def test_eh_hipotenusa(entrada, expected):
    assert eh_hipotenusa(entrada) == expected

@mark.parametrize('entrada, expected', [(25, 105)])
def test_soma_hipotenusa(entrada, expected):
    assert soma_hipotenusas(entrada) == expected