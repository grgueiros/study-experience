from vogal import vogal

def test_vogal():
    assert vogal('b') == False
    assert vogal('a') == True
    assert vogal('E') == True
