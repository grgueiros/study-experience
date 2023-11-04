import pytest
from maximo import maximo

@pytest.mark.parametrize('x,y,z,expected', [(30,14,10,30), (0,-1,1, 1)])
def test_maximo(x,y,z,expected):
    assert maximo(x,y,z) == expected