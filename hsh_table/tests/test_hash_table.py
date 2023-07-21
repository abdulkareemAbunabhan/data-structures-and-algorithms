import pytest
from hash_table import HashTable
@pytest.fixture
def hashtable():
    return HashTable()

def test_set_and_get(hashtable):
    hashtable.Set("key1", "value1")
    hashtable.Set("key2", "value2")
    hashtable.Set("key3", "value3")

    assert hashtable.GetKeyValue("key1") == "the value of key1 is value1"
    assert hashtable.GetKeyValue("key2") == "the value of key2 is value2"
    assert hashtable.GetKeyValue("key3") == "the value of key3 is value3"

def test_get_nonexistent_key(hashtable):
    assert hashtable.GetKeyValue("nonexistent_key") == "Not exist"

def test_all_keys(hashtable):
    hashtable.Set("key1", "value1")
    hashtable.Set("key2", "value2")
    hashtable.Set("key3", "value3")

    expected_keys = ["key1", "key2", "key3"]
    assert hashtable.AllKeys() == expected_keys

def test_collision_handling(hashtable):
    # Set two keys that will have the same hash value (collision)
    hashtable.Set("key1", "value1")
    hashtable.Set("key4", "value4")

    # Retrieve values from the colliding bucket
    assert hashtable.GetKeyValue("key1") == "the value of key1 is value1"
    assert hashtable.GetKeyValue("key4") == "the value of key4 is value4"

def test_hashing(hashtable):
    hashed_index = hashtable.CustomHash("key1")
    assert hashed_index in range(hashtable.size)

    hashed_index = hashtable.CustomHash("key5")
    assert hashed_index in range(hashtable.size)

    hashed_index = hashtable.CustomHash("key10")
    assert hashed_index in range(hashtable.size)
