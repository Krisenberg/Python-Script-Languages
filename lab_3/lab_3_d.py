from lab_2_d import get_entries_by_code
from lab_2_b import sort_log
import datetime
import sys

def print_dict_entry_dates(dicIp):
    for ip in dicIp:
        print("Host: " + ip)
        print("Numer of requests: " + str(len(dicIp[ip])))
        sort_by_date(dicIp[ip])
        print("First request date: " + str(dicIp[ip][0]['datetime']))
        print("Last request date: " + str(dicIp[ip][-1]['datetime']))
        print("Ratio: " + str(code_ratio(dicIp[ip])))
        print()
        
def sort_by_date(dicList):
    dicList.sort(key=lambda x: x['datetime'])
        
def code_ratio(dicList):
    i200 = 0
    for dic in dicList:
        if dic['code'] == 200:
            i200 += 1
    return i200 / len(dicList)

if __name__ == "__main__":
    dic = eval(sys.stdin.readline())
    print_dict_entry_dates(dic)