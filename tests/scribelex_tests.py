from src.scribelex import *


def test_shift():
    assert shift('a') == ('a', '')
    assert shift('hello') == ('h', 'ello')
    assert shift('12345') == ('1', '2345')
    assert shift('') is False
