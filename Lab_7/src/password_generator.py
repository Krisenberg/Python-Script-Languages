import string
import random

# Third task

class PasswordGenerator:
    def __init__(self, length, count, charset=(string.ascii_letters + string.digits), seed=100):
        self.length = length
        self.charset = charset
        self.count = count
        self.i = 0
        random.seed(seed)

    def __iter__(self):
        self.i = 0
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