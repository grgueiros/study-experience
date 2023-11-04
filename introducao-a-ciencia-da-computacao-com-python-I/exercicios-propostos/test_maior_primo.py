from maior_primo import maior_primo

def test_maior_primo_100():
    assert maior_primo(100) == 97

def test_maior_primo_7():
    assert maior_primo(7) == 7

def test_maior_primo_961():
    assert maior_primo(961) == 953