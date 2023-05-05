import functools
import random

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





# Second task

def forall(pred, iterable):
    return all(map(pred, iterable))

def exists(pred, iterable):
    return any(map(pred, iterable))

def atleast(n, pred, iterable):
    return len(list(filter(pred, iterable))) >= n

def atmost(n, pred, iterable):
    return len(list(filter(pred, iterable))) <= n

# # Test task 2
# if __name__ == "__main__":
#     iterable = [1,2,3,4,5,6,7,8,9,10]
#     pred = lambda x: x > 0
#     n = 6
#     print(forall(pred, iterable))
#     print(exists(pred, iterable))
#     print(atleast(n, pred, iterable))
#     print(atmost(n, pred, iterable))

# Third task

class PasswordGenerator:
    def __init__(self, length, charset, count):
        self.length = length
        self.charset = charset
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.count:
            self.i += 1
            return ''.join(random.choice(self.charset) for i in range(self.length))
        else:
            raise StopIteration
        
# # Test task 3
# if __name__ == "__main__":
#     password_generator = PasswordGenerator(20, "abc", 4)
#     print(next(password_generator))
#     for password in password_generator:
#         print(password)
#     print(next(password_generator))

# Fourth task

def make_generator(f):
    def generator():
        i = 1
        while True:
            yield f(i)
            i += 1
    return generator

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# # Test task 4
# if __name__ == "__main__":
#     print("Fibonacci:")
#     generator_f = make_generator(fibonacci)
#     generator_f = generator_f()
#     for i in range (10):
#         print(next(generator_f))
#     print("Lambda:")
#     generator_l = make_generator(lambda x: x+1)
#     generator_l = generator_l()
#     for i in range (10):
#         print(next(generator_l))

# Fifth task

def make_generator_mem(f):
    @functools.cache
    def memoized_f(n):
        return f(n)
    return make_generator(memoized_f)

        
# # Test task 5
# if __name__ == "__main__":
#     print("Fibonacci:")
#     generator_f = make_generator_mem(fibonacci)
#     generator_f = generator_f()
#     for i in range (10):
#         print(next(generator_f))
#     print("Lambda:")
#     generator_l = make_generator_mem(lambda x: x+1)
#     generator_l = generator_l()
#     for i in range (10):
#         print(next(generator_l))
    
# Sixth task

