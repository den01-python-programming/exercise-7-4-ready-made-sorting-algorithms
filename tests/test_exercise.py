import pytest
from src.exercise import sort_integers, sort_strings

def test_exercise():
    numbers = [3,6,2,7,1]
    sort_integers(numbers)

    assert numbers == [1,2,3,6,7]

    strings = ["Hello","Ada","Lovelace"]
    sort_strings(strings)

    assert strings == ["Ada","Hello","Lovelace"]
