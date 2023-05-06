from lab_3_b import log_to_dic
import sys
import datetime

def get_addrs(dicIp):
    return dicIp.keys()

if __name__ == "__main__":
    dic = eval(sys.stdin.readline())
    print(get_addrs(dic))