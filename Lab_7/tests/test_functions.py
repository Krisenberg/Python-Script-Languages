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