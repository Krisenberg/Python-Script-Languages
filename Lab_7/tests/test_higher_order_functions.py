import pytest
import sys

#insert the path of modules folder
sys.path.append("C:\\Users\\Kris\\Documents\\Studia\\Semestr_IV\\Jezyki_skryptowe_L\\Laboratoria\\Lab_7")

from src import higher_order_functions

@pytest.mark.parametrize(
    "pred, iterable, result",
    [
        (lambda x: x>0, [1,2,3,4,5,6,7,8,9,10], True),
        (lambda x: x>0, [1,2,0,4,5,6,7,8,9,10], False),
        (lambda x: x<=0, [-10], True),
        (lambda x: x<=0, [], True)
    ] 
)
def test_forall(pred, iterable, result):
    assert higher_order_functions.forall(pred, iterable) == result

@pytest.mark.parametrize(
    "pred, iterable, result",
    [
        (lambda x: x>0, [1,2,3,4,5,6,7,8,9,10], True),
        (lambda x: x>0, [1,2,0,4,5,6,7,8,9,10], True),
        (lambda x: x>10, [1,2,0,4,5,6,7,8,9,10], False),
        (lambda x: x<=0, [-10], True),
        (lambda x: x<=0, [], False)
    ] 
)
def test_exists(pred, iterable, result):
    assert higher_order_functions.exists(pred, iterable) == result

@pytest.mark.parametrize(
    "n, pred, iterable, result",
    [
        (9, lambda x: x>0, [1,2,3,4,5,6,7,8,9,10], True),
        (10, lambda x: x>0, [1,2,3,4,5,6,7,8,9,10], True),
        (0, lambda x: x>10, [1,2,0,4,5,6,7,8,9,10], True),
        (1, lambda x: x<=0, [-10], True),
        (1, lambda x: x<=0, [], False),
        (0, lambda x: x<=0, [], True)
    ] 
)
def test_atleast(n, pred, iterable, result):
    assert higher_order_functions.atleast(n, pred, iterable) == result

@pytest.mark.parametrize(
    "n, pred, iterable, result",
    [
        (9, lambda x: x>0, [1,2,3,4,5,6,7,8,9,10], False),
        (10, lambda x: x>0, [1,2,3,4,5,6,7,8,9,10], True),
        (0, lambda x: x>10, [1,2,0,4,5,6,7,8,9,10], True),
        (1, lambda x: x<=0, [-10], True),
        (1, lambda x: x<=0, [], True),
        (0, lambda x: x<=0, [], True)
    ] 
)
def test_atmost(n, pred, iterable, result):
    assert higher_order_functions.atmost(n, pred, iterable) == result