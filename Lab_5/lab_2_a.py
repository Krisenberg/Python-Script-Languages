import sys
from datetime import datetime
import re

def dicFromLine(line):
    namesList = ['datetime','host','component','pid','message']
    list = line.split()
    stringDate = list[0] + " " + list[1] + " " + " " + list[2]
    # fullDate is a datetime object in format "1900 Jan 01 00:00:00" (year is not important)
    fullDate = datetime.strptime(stringDate, "%b %d %H:%M:%S")
    # date is a string in format "Jan 01 00:00:00"
    # date = fullDate.strftime("%b %d %H:%M:%S")
    # host is a string 
    host = list[3]
    # componentWithPid is a string in format "component[pid]:"
    componentWithPid = list[4].split('[')
    #component is a string
    component = componentWithPid[0]
    # pid is a string
    pid = componentWithPid[1][:-1]
    # message is a long string with all the rest of the line
    message = " ".join(list[5:])
    # retList = [date, host, component, pid, message]
    retList = [fullDate, host, component, pid, message]
    combinedList = zip(namesList, retList)
    return dict(combinedList)

def dictFromLine(line):
    pattern = r'^(.+)\s(\d+)\s(\d{2}:\d{2}:\d{2})\s(.+)\s(sshd)\[(\d+)\]:\s(.+)$'
    match = re.match(pattern, line)
    stringDate = match.group(1) + ' ' + match.group(2) + ' ' + match.group(3)
    # fullDate is a datetime object in format "1900 Jan 01 00:00:00" (year is not important)
    fullDate = datetime.strptime(stringDate, "%b %d %H:%M:%S")
    host = match.group(4)
    component = match.group(5)
    pid = match.group(6)
    message = match.group(7)
    namesList = ['datetime','host','component','pid','message']
    valuesList = [fullDate, host, component, int(pid), message]
    return dict(zip(namesList, valuesList))

def get_ipv4s_from_log(line):
    pattern = r'^(.+)\s(\d+)\s(\d{2}:\d{2}:\d{2})\s(.+)\s(sshd)\[(\d+)\]:\s(.+)$'
    match1 = re.match(pattern, line)
    message = match1.group(7)
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ipv4s = re.findall(ipv4_pattern, message)
    return ipv4s


def readLogs(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        logs = []
        for line in lines:
            logs.append(dicFromLine(line))
        return logs
    
if _name_ == "_main_":
    filename = sys.argv[1]
    logs = readLogs(filename)
    print(logs)