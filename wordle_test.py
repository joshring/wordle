import pytest

from wordle import wordle_clue_1, wordle_clue_2, wordle_clue_3


def test_wordle_clue_1():
    assert wordle_clue_1(hidden="shear", candidate="knead") == "--xx-"


def test_wordle_clue_2():
    assert wordle_clue_2(hidden="ahead", candidate="dream") == "o-xx-"


def test_wordle_clue_3():
    assert wordle_clue_1(hidden="shear", candidate="knead") == "--xx-"
    assert wordle_clue_2(hidden="ahead", candidate="dream") == "o-xx-"
    assert wordle_clue_3(hidden="livid", candidate="pills") == "-xo--"
    assert wordle_clue_3(hidden="mardy", candidate="giddy") == "---xx"
    assert wordle_clue_3(hidden="aaaay", candidate="haada") == "-xx-o"
    assert wordle_clue_3(hidden="haada", candidate="aaaay") == "oxx--"
    assert wordle_clue_3(hidden="hrady", candidate="hardy") == "xooxx"
