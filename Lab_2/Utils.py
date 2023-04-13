import math
import sys
import datetime
import re

def linkValidation(link):
    pattern = r"^.+ - - \[\d{2}/Jul/1995:\d{2}:\d{2}:\d{2} -\d{4}\] \"(GET|POST|HEAD|PUT|DELETE|OPTIONS|CONNECT|TRACE) .+ HTTP/\d\.\d\" \d{3} \d+$"
    return re.match(pattern, link)
    # if match:
    #     return True
    # return False

def getCode(line):
    code = 0
    try:
        split1 = line.split('"', 2)
        split2 = split1[2].strip()
        code = split2.split(' ')[0]
    except IndexError:
        return 0
    try:
        return int (code)
    except ValueError:
        return 0

def getDataSize(line):
    try:
        split1 = line.split('"', 2)
        split2 = split1[2].strip()
        dataSize = split2.split(' ')[1]
        try:
            return int(dataSize)
        except ValueError:
            return 0
    except IndexError:
        return 0
    
def getPath(line):
    try:
        split1 = line.split('"')
        split2 = split1[1].split(' ')
        path = split2[1]
        return path
    except IndexError:
        return ""
    
def getHour(line):
    try:
        split1 = line.split(":")
        hourStr = split1[1]
        try:
            return int(hourStr)
        except ValueError:
            return -1
    except IndexError:
        return -1
    
def getDate(line):
    try:
        pos1 = line.find("[") + 1
        pos2 = line.find("/")
        day = line[pos1 : pos2]
        try:
            dayInt = int(day)
            return datetime.date(1995, 7, dayInt)
        except ValueError:
            return -1
    except IndexError:
        return -1


def countLinesCode(codeToBeCompared):
    reducedLinesNumber = 0

    while True:
        try:
            line = input()
            if (linkValidation(line)):
                code = getCode(line)
                if (code == codeToBeCompared):
                    reducedLinesNumber += 1
        except EOFError:
            break
    return reducedLinesNumber