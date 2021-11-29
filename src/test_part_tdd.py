import pytest
from src.part_tdd import anagram, palindroom, leeftijd
# Schrijf hier testen voor je oefeningen.
# Begin iedere testfunctie met naam "test_" gevolgd door de
# naam van de functie die je gaat testen, gevold door 
# een naam die aangeeft wat je gaat testen.
# 
# B.v.
# Om een functie "kwadraat" te testen, kan je als eerste test
# een functie met naam "test_kwadraat_2" die test dat het
# kwadraat van 2 4 is.

TESTDATA_ANAGRAMS = [
    ("tol", "lot"),
    ("omicron", "moronic"),
    ("evil", "vile"),
    ("kakstoel", "koelkast"),
    ("New York Times", "monkeys write"),
    ("Church of Scientology", "rich chosen goofy cult"),
    ("McDonald's restaurants", "Uncle Sam's standard rot"),
    ("William Shakespeare", "I am a weakish speller"),
    ("Tom Marvolo Riddle", "I am Lord Voldemort"),
]

@pytest.mark.parametrize("word1,word2", TESTDATA_ANAGRAMS)
def test_anagram(word1, word2):
    result = anagram(word1, word2)
    assert result is True

TESTDATA_NOT_ANAGRAMS = [
    ("tol", "lol"),
    ("New York Times", "monkey write"),
    ("Church of Scientology", "rich-choosen goofy cult"),
    ("McDonald's restaurant", "Uncle Sam's standard rot"),
    ("William Shakespeare", "I am a weakish speler"),
]

@pytest.mark.parametrize("word1,word2", TESTDATA_NOT_ANAGRAMS)
def test_are_not_anagrams(word1, word2):
    result = anagram(word1, word2)
    assert result is False

def test_palindroom_lol():
    result = palindroom("lol")
    assert result is True

def test_palindroom_tol():
    result = palindroom("tol")
    assert result is False

def test_palindroom_meetsysteem():
    result = palindroom("meetsysteem")
    assert result is True

def test_palindroom_stormrots():
    result = palindroom("stromrots")
    assert result is False

def test_palindroom_stormrot():
    result = palindroom("stormrot")
    assert result is False

def test_leeftijd_44():
    result = leeftijd(1976, 12, 20)
    assert result == 44

def test_leeftijd_45():
    result = leeftijd(1976, 11, 22)
    assert result == 45

def test_leeftijd_14():
    result = leeftijd(2007, 8, 6)
    assert result == 14

def test_leeftijd_10():
    result = leeftijd(2011, 9, 21)
    assert result == 10

def test_leeftijd_7():
    result = leeftijd(2014, 3, 4)
    assert result == 7

def test_leeftijd_74():
    result = leeftijd(1947, 11, 11)
    assert result == 74

def test_leeftijd_75():
    result = leeftijd(1946, 2, 21)
    assert result == 75

def test_leeftijd_51():
    result = leeftijd(1970, 8, 22)
    assert result == 51

