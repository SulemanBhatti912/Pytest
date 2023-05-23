import pytest

def test_one_plus_one():
    assert 1+1==2

def test_one_plus_two():
    assert 1+2==0

def test_one_plus_three():
    assert 1 + 3 == 4

def division_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num=1/0
    assert 'Division by zero' in str(e.value)