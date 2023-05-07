import functools
import time

# Fourth task

def make_generator(f):
    def generator():
        i = 1
        while True:
            yield f(i)
            i += 1
    return generator

def fibonacci(n):
    if n==0 or n==1:
        return n
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

global_mem_f=(lambda x: x, False)

def memoized_f(f):
    @functools.cache
    def memoized(n):
        return f(n)
    return memoized

def make_generator_mem(f):
    global global_mem_f
    if global_mem_f[1]==False:
        global_mem_f = (memoized_f(f), True)
    return make_generator(global_mem_f[0])

        
# Test task 5
if __name__ == "__main__":
    print("Fibonacci:")
    generator_f = make_generator_mem(fibonacci)
    generator_f = generator_f()
    for i in range (10):
        print(next(generator_f))
    print("Lambda:")
    generator_l = make_generator_mem(lambda x: x+1)
    generator_l = generator_l()
    for i in range (10):
        print(next(generator_l))