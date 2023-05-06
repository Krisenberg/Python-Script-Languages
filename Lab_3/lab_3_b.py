from lab_3_a import entry_to_dict
import sys
import datetime

def log_to_dic(tupleList):
    dic={}
    for tuple in tupleList:
        if(dic.get(tuple[0])!=None):
            dic[tuple[0]].append(entry_to_dict(tuple))
        else:
            dic[tuple[0]]=[entry_to_dict(tuple)]
    return dic

if __name__ == "__main__":
    tupleList = [eval(line) for line in sys.stdin.readlines()]
    print(log_to_dic(tupleList))
