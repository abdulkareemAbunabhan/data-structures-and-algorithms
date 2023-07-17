import pytest
from hasher import *
from hashmap_left_join import left_join

def test_left_join():
    # Test case 1: Both hash maps have common keys (with synonyms and antonyms)
    synonyms=HashTable()
    antonyms=HashTable()
    synonyms.Set('happy','joyful')
    synonyms.Set('big','large')
    synonyms.Set('small','tiny')
    antonyms.Set('happy','sad')
    antonyms.Set('big','small')
    antonyms.Set('small','big')
    assert left_join(synonyms, antonyms) == [['happy', 'joyful', 'sad'], ['big', 'large', 'small'], ['small', 'tiny', 'big']]

    # Test case 2: Only one key is common (with synonyms and antonyms)
    # synonyms = {'happy': 'joyful', 'big': 'large', 'small': 'tiny'}
    # antonyms = {'good': 'bad', 'big': 'small', 'small': 'big'}
    # assert left_join(synonyms, antonyms) == [['happy', 'joyful', None], ['big', 'large', 'small'], ['small', 'tiny', 'big']]

    # # Test case 3: No common keys (with synonyms and antonyms)
    # synonyms = {'happy': 'joyful', 'big': 'large', 'small': 'tiny'}
    # antonyms = {'good': 'bad', 'fast': 'slow', 'hot': 'cold'}
    # assert left_join(synonyms, antonyms) == [['happy', 'joyful', None], ['big', 'large', None], ['small', 'tiny', None]]

    # # Test case 4: Empty synonyms hash map
    # synonyms = {}
    # antonyms = {'happy': 'sad', 'big': 'small'}
    # assert left_join(synonyms, antonyms) == []

    # # Test case 5: Empty antonyms hash map
    # synonyms = {'happy': 'joyful', 'big': 'large'}
    # antonyms = {}
    # assert left_join(synonyms, antonyms) == [['happy', 'joyful', None], ['big', 'large', None]]