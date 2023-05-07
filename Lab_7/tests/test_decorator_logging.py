import pytest
import sys
import time
import logging

#insert the path of modules folder
sys.path.append("C:\\Users\\Kris\\Documents\\Studia\\Semestr_IV\\Jezyki_skryptowe_L\\Laboratoria\\Lab_7")

from src import decorator_logging

@decorator_logging.log(logging.DEBUG)
def func(x,y):
    return x**y + y**x


@decorator_logging.log(logging.CRITICAL)
class DummyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def do_something(self):
        print(f"Instance named {self.name} is doing something with value: {self.value}.")
""" Tests 
    func(2,3)
    func(10,2)
    A = DummyClass("Test A", 10)
    B = DummyClass("Test B", 12345) """