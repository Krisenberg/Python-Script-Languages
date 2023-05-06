import math
import sys
import datetime
import re

def linkValidation(link):
    #pattern = r"^.+ - - \[\d{2}/Jul/1995:\d{2}:\d{2}:\d{2} -\d{4}\] \"(GET|POST|HEAD|PUT|DELETE|OPTIONS|CONNECT|TRACE) .+ HTTP/\d\.\d\" \d{3} \d+$"
    pattern = r"^(.+) - - \[(\d{2}/Jul/1995:\d{2}:\d{2}:\d{2} -\d{4})\] \"([A-Z]{3,}) (.+ HTTP/\d\.\d)\" (\d{3}) (\d+)$"
    return re.match(pattern, link)

def validateAddress(key):
    if not(any(char.isalpha() for char in key)):
        patternIP = r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"
        return bool(re.match(patternIP, key))
    return True

def validateCode(key):
    patternCode = r"^\d{1,3}$"
    return bool(re.match(patternCode, key))

def stringToTupleList():
    list = []
    while True:
        try:
            line = input()
            list.append(tuple(line))
        except EOFError:
            break
    return list