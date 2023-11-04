import pytest
from primos_entre_2_e_n import eh_primo, n_primos


@pytest.mark.parametrize('entrada, expected', [
    (2, True),
    (3, True),
    (4, False),
    (7, True),
    (9, False),
    (13, True),
    (19, True),
    (18, False)
])
def test_eh_primo(entrada, expected):
    assert eh_primo(entrada) == expected


@pytest.mark.parametrize('entrada, expected', [
    (2, 1),
    (3, 2),
    (4, 2),
    (121, 30),
])
def test_n_primos(entrada, expected):
    assert n_primos(entrada) == expected