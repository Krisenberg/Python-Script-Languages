import re, sys, datetime
from Utils import validateAddress

def get_entries_by_addr(tupleList, key):
    if validateAddress(key):
        return [entry for entry in tupleList if entry[0]==key]
    return None

if __name__ == "__main__":
    tupleList = [eval(line) for line in sys.stdin.readlines()]
    key = sys.argv[1]
    list = get_entries_by_addr(tupleList, key)
    for line in list:
        print(line)