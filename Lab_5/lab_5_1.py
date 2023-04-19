import sys
import re
from lab_5_2 import *
from lab_5_3 import logLine

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

# def printLogs(logs):
#     for index, log in enumerate(logs):
#         print(f'{index}:  {log}')

def printLogs(logs, **kwargs):
    if ('number' in kwargs):
        for i in range(1,kwargs.get('number')+1):
            print(f'{i}:  {logs[i-1]}')
    else:
        for index, log in enumerate(logs):
            print(f'{index}:  {log}')

# if __name__ == "__main__":
#     filename = sys.argv[1]
#     functionName = sys.argv[2]
#     function = getattr(sys.modules[__name__], functionName)
#     which = int(sys.argv[3])
#     logs = readLogs(filename, parse_ssh_log)
#     if (which == 1): print(logs)
#     elif (which == 2): print(parseLogs(logs,function))
#     elif (which == 3): print(parseMessages(logs, function))
#     else: print("3rd argument must be 1, 2 or 3")   