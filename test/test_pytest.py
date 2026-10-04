import pytest
from src import morse


def test_encode():
    assert morse.encode("SOS") == "... --- ..."
    assert morse.encode("sos") == "... --- ..."
    assert morse.encode("HI THERE") == ".... .. / - .... . .-. ."
    assert morse.encode("123") == ".---- ..--- ...--"
    assert morse.encode("") == ""


def test_encode_invalid():
    with pytest.raises(ValueError):
        morse.encode(123)
    with pytest.raises(ValueError):
        morse.encode("HELLO!")


def test_decode():
    assert morse.decode("... --- ...") == "SOS"
    assert morse.decode(".... .. / - .... . .-. .") == "HI THERE"
    assert morse.decode(".---- ..--- ...--") == "123"
    assert morse.decode("") == ""


def test_decode_invalid():
    with pytest.raises(ValueError):
        morse.decode(None)
    with pytest.raises(ValueError):
        morse.decode("...---...")


def test_round_trip():
    assert morse.decode(morse.encode("Hello World 2026")) == "HELLO WORLD 2026"


def test_count_signals():
    assert morse.count_signals("... --- ...") == (6, 3)
    assert morse.count_signals("") == (0, 0)
    assert morse.count_signals(".-") == (1, 1)


def test_add_morse():
    assert morse.add_morse("..---", "...--") == "....."              # 2 + 3 = 5
    assert morse.add_morse(".---- -----", "-----") == ".---- -----"  # 10 + 0 = 10
    assert morse.add_morse("---..", "--...") == ".---- ....."        # 8 + 7 = 15


def test_add_morse_invalid():
    with pytest.raises(ValueError):
        morse.add_morse(".-", "..---")  # "A" is not a number
