from remove_repetidos import remove_repetidos

def test_remove_repetidos () :
    assert remove_repetidos([2, 4, 2, 2, 3, 3, 1]) == [1, 2, 3, 4]