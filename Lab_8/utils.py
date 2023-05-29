import re
from datetime import datetime

def get_user_from_log(message):
    # If message is empty return None
    if message is None:
        return None
    # Define regex pattern for username
    username_pattern = r"user (\w+)"
    match = re.search(username_pattern, message)
    if match:
        return match.group(1)
    # If previous pattern didn't match try another one
    else:
        username_pattern = r"user=(\w+)"
        match = re.search(username_pattern, message)
        if match:
            return match.group(1)
        # If previous pattern didn't match try another one
        else:
            username_pattern = r"for (\w+)"
            match = re.search(username_pattern, message)
            if match:
                return match.group(1)
    return None


# Function that parses a log represented by a string to a dictionary
def parse_ssh_log(log_string):
    # Define regex pattern
    pattern = r'^(.+)\s(\d+)\s(\d{2}:\d{2}:\d{2})\s(.+)\s(sshd)\[(\d+)\]:\s(.+)$'
    match = re.match(pattern, log_string)
    stringDate = match.group(1) + ' ' + match.group(2) + ' ' + match.group(3)
    # fullDate is a datetime object in format "1900 Jan 01 00:00:00" (year is not important)
    date = datetime.strptime(stringDate,"%b %d %H:%M:%S")
    component = match.group(5)
    pid = match.group(6)
    message = match.group(7)
    host = get_user_from_log(message)
    namesList = ['timestamp','host','component','pid','message']
    valuesList = [date, host, component, int(pid), message]
    return dict(zip(namesList, valuesList))