import sys
import re
from lab_5_2 import *
from lab_5_3 import logLine

# def dicFromLine(line):
#     namesList = ['datetime','host','component','pid','message']
#     list = line.split()
#     stringDate = list[0] + " " + list[1] + " " + " " + list[2]
#     # fullDate is a datetime object in format "1900 Jan 01 00:00:00" (year is not important)
#     fullDate = datetime.strptime(stringDate, "%b %d %H:%M:%S")
#     # date is a string in format "Jan 01 00:00:00"
#     # date = fullDate.strftime("%b %d %H:%M:%S")
#     # host is a string 
#     host = list[3]
#     # componentWithPid is a string in format "component[pid]:"
#     componentWithPid = list[4].split('[')
#     #component is a string
#     component = componentWithPid[0]
#     # pid is a string
#     pid = componentWithPid[1][:-1]
#     # message is a long string with all the rest of the line
#     message = " ".join(list[5:])
#     # retList = [date, host, component, pid, message]
#     retList = [fullDate, host, component, pid, message]
#     combinedList = zip(namesList, retList)
#     return dict(combinedList)

# Function that takes a file and returns its logs as a structure given by function
def readLogs(filename, function, logger):
    with open(filename, 'r') as f:
        lines = f.readlines()
        logs = []
        for line in lines:
            logs.append(function(line))
            logLine(line, logger)
        return logs
    
# Function that takes logs in any form and returns a list with info about each row
def parseLogs(logs, function):
    parsed_logs = []
    for log in logs:
        parsed_logs.append(function(log))
    return parsed_logs

# Function that take logs in any from and returns a list with info about each message
def parseMessages(logs, function):
    parsed_messages = []
    for log in logs:
        parsed_messages.append(function(log['message']))
    return parsed_messages

def printLogs(logs):
    for index, log in enumerate(logs):
        print(f'{index}:  {log}')

def printLogs(logs, number):
    for i in range(1,number+1):
        print(f'{i}:  {logs[i-1]}')

if __name__ == "__main__":
    filename = sys.argv[1]
    functionName = sys.argv[2]
    function = getattr(sys.modules[__name__], functionName)
    which = int(sys.argv[3])
    logs = readLogs(filename, parse_ssh_log)
    if (which == 1): print(logs)
    elif (which == 2): print(parseLogs(logs,function))
    elif (which == 3): print(parseMessages(logs, function))
    else: print("3rd argument must be 1, 2 or 3")   