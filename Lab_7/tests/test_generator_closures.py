import pytest
import sys
import time

#insert the path of modules folder
sys.path.append("C:\\Users\\qmati\\Documents\\Krisenberg\\Python-Script-Languages\\Lab_7")

from src import generator_closures

def test_fib_nums():
    sys.setrecursionlimit(1000)
    fib_nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    fib_generator = generator_closures.make_generator(generator_closures.fibonacci)()
    nums = []
    for i in range(10):
        nums.append(next(fib_generator))
    assert nums == fib_nums

def test_fib_nums_without_cache():
    sys.setrecursionlimit(1000)
    fib_generator = generator_closures.make_generator(generator_closures.fibonacci)()
    last_num1 = 0
    start_time_1 = time.time()
    for i in range(35):
        last_num1 = next(fib_generator)
    end_time_1 = time.time()
    fib_generator = generator_closures.make_generator(generator_closures.fibonacci)()
    last_num2 = 0
    start_time_2 = time.time()
    for i in range(35):
        last_num2 = next(fib_generator)
    end_time_2 = time.time()

    total_1 = end_time_1 - start_time_1
    total_2 = end_time_2 - start_time_2

    assert (last_num1 == 9227465 and last_num2 == 9227465 and total_1 > 3 and total_2 > 3)

def test_fib_nums_with_cache():
    sys.setrecursionlimit(1000)
    fib_generator = generator_closures.make_generator_mem(generator_closures.fibonacci)()
    last_num1 = 0
    start_time_1 = time.time()
    for i in range(35):
        last_num1 = next(fib_generator)
    end_time_1 = time.time()
    fib_generator = generator_closures.make_generator_mem(generator_closures.fibonacci)()
    last_num2 = 0
    start_time_2 = time.time()
    for i in range(35):
        last_num2 = next(fib_generator)
    end_time_2 = time.time()

    total_1 = end_time_1 - start_time_1
    total_2 = end_time_2 - start_time_2

    assert (last_num1 == 9227465 and last_num2 == 9227465 and total_1 > 3 and total_2 < 0.01)