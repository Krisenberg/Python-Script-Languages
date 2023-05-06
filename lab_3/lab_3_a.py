import sys, datetime

def entry_to_dict(entryTuple):
    namesList = ['host','datetime','request','path','code','bytes']
    combinedList = zip(namesList, entryTuple)
    return dict(combinedList)

if __name__ == "__main__":
    line = sys.stdin.readlines()
    entry = eval(line[0])
    print(entry_to_dict(entry))