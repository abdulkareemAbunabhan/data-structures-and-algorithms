import pytest 
from hash_map_repeated import find_the_first_repeated , all_words_count , the_most_repeated_word_list

def test1(): #normal input , standard case
    assert "the"==(find_the_first_repeated("the hardwork is the best medicine"))

def test2(): # one letter repeated 
    assert "a" == find_the_first_repeated("hello world with a repeated letter like a")

def test6(): # the repeated is a number
    assert "3" == find_the_first_repeated("1 2 3 4 5 6 7 8 9 0 3 3 5 6 7 8 9 0")

def test_all_words_count():
    # Normal input with repeated words
    assert {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1} == all_words_count("the quick brown fox jumps over the lazy")

    # # Input with punctuation marks
    assert {'hello': 3, 'world': 3, 'welcome': 2} == all_words_count("hello, world hello. world, hello world. welcome, welcome")

    # Empty string
    assert {} == all_words_count("")

    # String with only one word
    assert {'hello': 1} == all_words_count("hello")

    # String with repeated words and trailing punctuation
    assert {'hello': 2, 'world': 2, 'sameer': 1} == all_words_count("hello, world, hello. world sameer")  

def test_the_most_repeated_word_list():
    # Normal input with repeated words
    assert ['repeated'] == the_most_repeated_word_list("repeated words are repeated")

    # Input with punctuation marks
    assert ['hello', 'world'] == the_most_repeated_word_list("hello, world hello. world, hello world. welcome, welcome")

    # Empty string
    assert [] == the_most_repeated_word_list("")

    # String with only one word
    assert ['hello'] == the_most_repeated_word_list("hello")

    # String with repeated words and trailing punctuation
    assert ['hello', 'world'] == the_most_repeated_word_list("hello, world, hello. world sameer")
