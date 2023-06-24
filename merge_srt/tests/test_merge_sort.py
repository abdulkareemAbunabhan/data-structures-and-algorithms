import pytest
from merge_sort import Mergesort
# Test case for Merge Sort
def test_merge_sort():
    # Test case 1: Empty list
    arr1 = []
    assert Mergesort(arr1) == []

    # Test case 2: List with one element
    arr2 = [5]
    assert Mergesort(arr2) == [5]

    # Test case 3: List with multiple elements
    arr3 = [9, 2, 7, 1, 5]
    assert Mergesort(arr3) == [1, 2, 5, 7, 9]

    # Test case 4: List with duplicate elements
    arr4 = [3, 6, 2, 9, 2, 3]
    assert Mergesort(arr4) == [2, 2, 3, 3, 6, 9]

    # Test case 5: List sorted in ascending order
    arr5 = [1, 2, 3, 4, 5]
    assert Mergesort(arr5) == [1, 2, 3, 4, 5]

    # Test case 6: List sorted in descending order
    arr6 = [5, 4, 3, 2, 1]
    assert Mergesort(arr6) == [1, 2, 3, 4, 5]

    # Test case 7: List with negative numbers
    arr7 = [-3, -7, 2, -1, 0]
    assert Mergesort(arr7) == [-7, -3, -1, 0, 2]

    # Test case 8: List with strings
    arr8 = ['banana', 'apple', 'cherry', 'date']
    assert Mergesort(arr8) == ['apple', 'banana', 'cherry', 'date']

    # Test case 9: List with empty strings
    arr9 = ['', 'abc', '', 'def', '']
    assert Mergesort(arr9) == ['', '', '', 'abc', 'def']