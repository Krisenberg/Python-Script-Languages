import pytest
import sys

#insert the path of modules folder
sys.path.append("C:\\Users\\Kris\\Documents\\Studia\\Semestr_IV\\Jezyki_skryptowe_L\\Laboratoria\\Lab_7")

from src import functions

@pytest.mark.parametrize(
    "full_name, acronym",
    [
        (["Zakład", "Ubezpieczeń", "Społecznych"], "ZUS"),
        (["Polski", "Związek", "Piłki", "Nożnej"], "PZPN"),
        (["Aaa", "bbb", "", "Dddd"], "AbD")
    ] 
)
def test_acronym(full_name, acronym):
    assert functions.acronym(full_name) == acronym


@pytest.mark.parametrize(
    "numbers, median",
    [
        ([1,1,19,2,3,4,4,5,1], 3),
        ([1,1,19,2,3,4,4,5,1,6], 3.5),
        ([4], 4),
        ([4,6], 5),
        ([6,4], 5),
        ([], 'List is empty!')
    ] 
)
def test_median(numbers, median):
    assert functions.median(numbers) == median

@pytest.mark.parametrize(
    "number, epsilon, start, sqrt",
    [
        (3, 0.1, 1, 1.75),
        (5, 0.01, 5, 2.238095238095238),
        (100, -2, 100, "x and epsilon must be greater or equal to 0"),
        (-4, 0.1, 100, "x and epsilon must be greater or equal to 0")
    ] 
)
def test_sqrt(number, epsilon, start, sqrt):
    assert functions.sqrt(number, epsilon, start) == sqrt

@pytest.mark.parametrize(
    "words, dict",
    [
        ("on i ona", {'o': ['on', 'ona'], 'n': ['on', 'ona'], 'i': ['i'], 'a': ['ona']}),
        ("ala ma kota, kot ma ale. am la ml al", 
         {'a': ['ala', 'ma', 'kota', 'ma', 'ale', 'am', 'la', 'al'],
          'l': ['ala', 'ale', 'la', 'ml', 'al'],
          'm': ['ma', 'ma', 'am', 'ml'],
          'k': ['kota', 'kot'],
          'o': ['kota', 'kot'],
          't': ['kota', 'kot'],
          'e': ['ale']})
    ] 
)
def test_make_alpha_dict(words, dict):
    assert functions.make_alpha_dict(words) == dict

@pytest.mark.parametrize(
    "seq, flat_list",
    [
        ([1, [2,3], [[4, 5], 6]], [1,2,3,4,5,6]),
        ([(1,1,(2,(3))), [(4),(5,(6,(7,[8,9,(10,11)])))]], [1,1,2,3,4,5,6,7,8,9,10,11])
    ] 
)
def test_flatten(seq, flat_list):
    assert functions.flatten(seq) == flat_list