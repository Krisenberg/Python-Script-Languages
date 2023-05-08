import functools
import random
import string

""" If the optional initializer is present, it is placed before the items of the iterable 
    in the calculation, and serves as a default when the iterable is empty. If initializer 
    is not given and iterable contains only one item, the first item is returned."""
def acronym(stringList):
    # firstLetters = list(map(lambda x: x[0] if len(x)>0 else '',stringList))
    # return functools.reduce(lambda x, y: x+y, firstLetters)
    return functools.reduce(lambda x, y: x+y[0].upper() if len(y)>0 else x+'', stringList, '')

def median(numbers):
    sorted_numbers = sorted(numbers)
    list_len = len(sorted_numbers)
    median_index = list_len // 2

    try:
        return sorted_numbers[median_index] if list_len % 2 == 1 else (sorted_numbers[median_index-1]+sorted_numbers[median_index])/2
    except IndexError:
        return "List is empty!"
    
def sqrt(x, epsilon=0.1, start=0):
    starting_point = random.uniform(0,x/2) if start<=0 else start
    def innerHelper (y):
        return y if y>=0 and abs(y**2 - x)<epsilon else innerHelper(0.5*(y+(x/y)))
    return (innerHelper(starting_point) if x>=0 and epsilon>=0 else "x and epsilon must be greater or equal to 0")


def make_alpha_dict(words):
    words = words.replace(',','')
    words = words.replace('.','')
    letters = set([words[i] for i in range(len(words)) if not (words[i].isspace())])
    dictionary = {key: list(filter(lambda word: key in word, words.split())) for key in letters}
    return dictionary

def flatten(inputList):
    return [elem for item in inputList for elem in flatten(item)] if (type(inputList) is list or type(inputList) is tuple) else [inputList]

