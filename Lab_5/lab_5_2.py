import sys, re

# # Function that takes a line from the log file and returns a dictionary with given keys
# def parse_ssh_log(log_string):
#     # Define regex patterns
#     regex_patterns = {
#         "timestamp": r"^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})",
#         "process_name": r"\b(\w+)\[\d+\]:",
#         "source_ip": r"\[([\d\.]+)\]",
#         "message": r"^\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\w+\s+\w+\[\d+\]:\s+(.*)"
#     }

#     # Initialize dictionary to store parsed log
#     log_dict = {}

#     # Iterate over regex patterns, apply them to the log string and store the result in the dictionary
#     for key, pattern in regex_patterns.items():
#         match = re.search(pattern, log_string)
#         if match:
#             log_dict[key] = match.group(1)

#     return log_dict

# Function that takes a line from the log file and returns a dictionary with given keys
def parse_ssh_log(log_string):
    # Define regex pattern
    pattern = r'^(.+)\s(\d+)\s(\d{2}:\d{2}:\d{2})\s(.+)\s(sshd)\[(\d+)\]:\s(.+)$'
    match = re.match(pattern, log_string)
    stringDate = match.group(1) + ' ' + match.group(2) + ' ' + match.group(3)
    # fullDate is a datetime object in format "1900 Jan 01 00:00:00" (year is not important)
    host = match.group(4)
    component = match.group(5)
    pid = match.group(6)
    message = match.group(7)
    namesList = ['timestamp','host','process_name','pid','message']
    valuesList = [stringDate, host, component, int(pid), message]
    return dict(zip(namesList, valuesList))

# Function that takes a log in form of a dictionary and returns a list of ip adresses in its message
def get_ipv4s_from_log(log_dictionary):
    # Define regex pattern for IP addresses
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    #ip_address_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    # Find all IP addresses in the log string
    ip_addresses = re.findall(ipv4_pattern, log_dictionary['message'])

    return ip_addresses

# Function that take a log in form of a dictionary and returns a username in its message
def get_user_from_log(log_dictionary):
    # Initialize message from fictionary
    message = log_dictionary.get("message")
    
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

# Function that takes a message as a string and returns its type as a string
def get_message_type(message):
    # Regex patterns for different types of messages
    success_pattern = re.compile(r'accepted\s+password', re.IGNORECASE)
    fail_pattern = re.compile(r'authentication\s+failure', re.IGNORECASE)
    disconnect_pattern = re.compile(r'received\s+disconnect', re.IGNORECASE)
    password_fail_pattern = re.compile(r'failed\s+password', re.IGNORECASE)
    username_fail_pattern = re.compile(r'invalid\s+user', re.IGNORECASE)
    break_in_pattern = re.compile(r'possible\s+break-in', re.IGNORECASE)
    
    # Check for matching patterns in the message
    if success_pattern.search(message):
        return "Authentication succeeded."
    elif fail_pattern.search(message):
        return "Authentication failed."
    elif disconnect_pattern.search(message):
        return "Disconnected."
    elif password_fail_pattern.search(message):
        return "Incorrect password."
    elif username_fail_pattern.search(message):
        return "Incorrect username."
    elif break_in_pattern.search(message):
        return "Break-in attempt."
    else:
        return "Other"