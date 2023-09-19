from lib.grammar_check import *
import pytest

def test_correct_with_full_stop():
    response = grammar_check("Today is tusday.")
    assert response == "It's grammatically correct"

def test_correct_with_exclamation_mark():
    response = grammar_check("Today is tusday!")
    assert response == "It's grammatically correct"

def test_correct_with_question_mark():
    response = grammar_check("Today is tusday?")
    assert response == "It's grammatically correct"

def test_correct_punc_but_not_cl():
    response = grammar_check("today is tuesday.")
    assert response == "Check your Capital Letters"

def test_incorrect_punctuation():
    response = grammar_check("Today is tuesday;")
    assert response == "Check your ending punctuation"

def test_double_incorrect():
    response = grammar_check("today is tuesday")
    assert response == "Please revise basic grammar"

def test_empty_string():
    with pytest.raises(Exception) as e:
        grammar_check("")
    error_message = str(e.value)
    assert error_message == "Please provide sentence"