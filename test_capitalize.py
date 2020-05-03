# test_capitalize.py

import pytest

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Pls give string arg')
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_nonstring():
    with pytest.raises(TypeError):
        capital_case(9)