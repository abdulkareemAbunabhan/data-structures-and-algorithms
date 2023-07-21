import pytest
from hashmap_left_join import left_join
from hash_table import *
def test_left_join():
    # Test case 1: Both hash maps have common keys (with synonyms and antonyms)
    # synonyms = {'happy': 'joyful', 'big': 'large', 'small': 'tiny'}
    synonyms=HashTable()
    synonyms.Set('happy','joyful')
    synonyms.Set('big','large')
    synonyms.Set('small','tiny')
    # antonyms = {'happy': 'sad', 'big': 'small', 'small': 'big'}
    antonyms=HashTable()
    antonyms.Set('happy','sad')
    antonyms.Set('big','small')
    antonyms.Set('small','big')
    assert left_join(synonyms, antonyms) == [['happy', 'joyful', 'sad'], ['big', 'large', 'small'], ['small', 'tiny', 'big']]

    # Test case 2: Only one key is common (with synonyms and antonyms)
    # synonyms = {'happy': 'joyful', 'big': 'large', 'small': 'tiny'}
    synonyms=HashTable()
    synonyms.Set('happy','joyful')
    synonyms.Set('big','large')
    synonyms.Set('small','tiny')
    # antonyms = {'good': 'bad', 'big': 'small', 'small': 'big'}
    antonyms=HashTable()
    antonyms.Set('good','bad')
    antonyms.Set('big','small')
    antonyms.Set('small','big')
    assert left_join(synonyms, antonyms) == [['happy', 'joyful', None], ['big', 'large', 'small'], ['small', 'tiny', 'big']]

    # Test case 3: No common keys (with synonyms and antonyms)
    # synonyms = {'happy': 'joyful', 'big': 'large', 'small': 'tiny'}
    synonyms=HashTable()
    synonyms.Set('happy','joyful')
    synonyms.Set('big','large')
    synonyms.Set('small','tiny')
    # antonyms = {'good': 'bad', 'fast': 'slow', 'hot': 'cold'}
    antonyms=HashTable()
    antonyms.Set('good','bad')
    antonyms.Set('fast','slow')
    antonyms.Set('hot','cold')
    assert left_join(synonyms, antonyms) == [['happy', 'joyful', None], ['big', 'large', None], ['small', 'tiny', None]]

    # Test case 4: Empty synonyms hash map
    synonyms = HashTable()
    # antonyms = {'happy': 'sad', 'big': 'small'}
    antonyms=HashTable()
    antonyms.Set('happy','sad')
    antonyms.Set('big','small')
    assert left_join(synonyms, antonyms) == []

    # Test case 5: Empty antonyms hash map
    # synonyms = {'happy': 'joyful', 'big': 'large'}
    synonyms=HashTable()
    synonyms.Set('happy','joyful')
    synonyms.Set('big','large')
    antonyms = HashTable()
    assert left_join(synonyms, antonyms) == [['happy', 'joyful', None], ['big', 'large', None]]