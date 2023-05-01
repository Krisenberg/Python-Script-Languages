from functools import reduce

def acronym(stringList):
    firstLetters = list(map(lambda x: x[0] if len(x)>0 else '',stringList))
    return reduce(lambda x, y: x+y, firstLetters)

def median(numbers):
    sorted_numbers = sorted(numbers)
    list_len = len(sorted_numbers)
    median_index = list_len // 2

    try:
        median = sorted_numbers[median_index] if list_len % 2 == 1 else (sorted_numbers[median_index-1]+sorted_numbers[median_index])/2
        return median
    except IndexError:
        return "List is empty!"
    
# def sqrt(x, epsilon):