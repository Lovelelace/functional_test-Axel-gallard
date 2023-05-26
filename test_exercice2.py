import pytest
from exercice2 import StringAnalyzer

def test_count_voyelles():
    analyzer = StringAnalyzer("ceci est un test unitaire pour les voyelles")
    assert analyzer.count_vowels() == 16

def test_count_consones():
    analyzer = StringAnalyzer("ceci est un test unitaire pour les consones")
    assert analyzer.count_consonants() == 20

def test_count_nombres():
    analyzer = StringAnalyzer("123456789")
    assert analyzer.count_digits() == 9

def test_count_mots():
    analyzer = StringAnalyzer("ceci est un test unitaire pour compter les mots")
    assert analyzer.count_words() == 9

def test_count_lignes():
    analyzer = StringAnalyzer("ceci est un test unitaire\n pour compter les lignes\n")
    assert analyzer.count_lines() == 3
