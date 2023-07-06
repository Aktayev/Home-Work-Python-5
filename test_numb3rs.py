from numb3rs import validate


def test_true():
    assert validate("1.2.3.4") == True
def test_folse():
    assert validate("1.2.255.266") == False
def test_except():
    assert validate("dog") == False