import sys, datetime

def print_entries(tupleList):
    for entry in tupleList:
        print(entry)

if __name__ == "__main__":
    tupleList = [eval(line) for line in sys.stdin.readlines()]
    print_entries(tupleList)