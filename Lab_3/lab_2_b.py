import sys,datetime

def sort_log(tupleList, elemToBeSortedBy):
    tupleList.sort(key = lambda x : x[elemToBeSortedBy])
    return tupleList

if __name__ == "__main__":
    tupleList = [eval(line) for line in sys.stdin.readlines()]
    key = int(sys.argv[1])
    try:
        list = sort_log(tupleList, key)
        for line in list:
            print(line)
    except IndexError:
        None
    
