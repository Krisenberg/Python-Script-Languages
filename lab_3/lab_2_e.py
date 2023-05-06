import re, sys, datetime

def get_failed_reads(tupleList, concatListsFlag=False):
    list4XX = [entry for entry in tupleList if entry[4]//100==4]
    list5XX = [entry for entry in tupleList if entry[4]//100==5]
    if (concatListsFlag):
        list4XX.extend(list5XX)
        return list4XX
    return list4XX, list5XX

if __name__ == "__main__":
    tupleList = [eval(line) for line in sys.stdin.readlines()]
    try:
        if (len(sys.argv)==2 and bool(sys.argv[1])):
            combinedList = get_failed_reads(tupleList, True)
            print("Combined list")
            for line in combinedList:
                print(line)
        else:
            list1, list2 = get_failed_reads(tupleList)
            print("List One")
            for line in list1:
                print(line)
            print("List Two")
            for line in list2:
                print(line)
    except TypeError:
                print("Invalid parameter")