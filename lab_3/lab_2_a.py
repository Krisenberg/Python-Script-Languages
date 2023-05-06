from Utils import linkValidation
import calendar
from datetime import datetime
import sys, re

# def split_log(line):
#     partition1 = line.split('- -')
#     host =  partition1[0].strip()
#     date = datetime.strptime(partition1[1][2:22],"%d/%b/%Y:%H:%M:%S")
#     zone = partition1[1][24:28]
#     partition2 = partition1[1].split('"')
#     request = partition2[1][0:3]
#     path = partition2[1][4:]
#     partition3 = partition2[2].strip().split(' ')
#     code = partition3[0]
#     dataSize = partition3[1]
#     return (host, date, int(zone), request, path, int(code), int(dataSize))


def split_log(line, match):
    # pattern = r"^(.+) - - \[(\d{2}/Jul/1995:\d{2}:\d{2}:\d{2}) (-\d{4})\] \"([A-Z]{3,}) (.+ HTTP/\d\.\d)\" (\d{3}) (\d+)$"
    # match = re.match(pattern, line)
    host =  match.group(1)
    date = datetime.strptime(match.group(2),"%d/%b/%Y:%H:%M:%S %z")
    request = match.group(3)
    path = match.group(4)
    code = match.group(5)
    dataSize = match.group(6)
    return (host, date, request, path, int(code), int(dataSize))


def read_log():
    tupleList = []
    faultyList = []
    while True:
        try:
            #line = sys.stdin.readline()
            line = input()
            match = linkValidation(line)
            if bool(match):
                try:
                    retTuple = split_log(line,match)
                    tupleList.append(retTuple)
                except (ValueError, IndexError):
                    faultyList.append(line)
        except EOFError:
            break
    return tupleList

if __name__ == "__main__":
    list = read_log()
    for line in list:
        print(line)