import re, sys, datetime
from Utils import validateCode

def get_entries_by_code(tupleList, key):
    if validateCode(key):
        return [entry for entry in tupleList if entry[5]==int(key)]
    return None

if __name__ == "__main__":
    tupleList = [eval(line) for line in sys.stdin.readlines()]
    key = sys.argv[1]
    list = get_entries_by_code(tupleList, key)
    for line in list:
        print(line)