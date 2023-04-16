from lab_5_1 import *
from lab_5_2 import *
import random
from datetime import datetime
import statistics

# Function that returns list of all users from log file
def prepare_users_list(logs):
    #Prepare users list
    users_list_with_none = parseLogs(logs, get_user_from_log)
    users_list_iterator = filter(lambda x: (x!=None), users_list_with_none)
    users_list = list(users_list_iterator)
    
    return users_list

# Function that returns n random logs from random user
def get_random_logs_from_random_user(logs, n):
    # Prepare logs and users list
    users_list = prepare_users_list(logs)
    
    # Select random user
    user = random.choice(users_list)
    
    # Select n random logs from selected user
    user_logs = []
    i = 0
    for log in logs:
        if user in log['message']:
            user_logs.append(log)
    try:
        random_logs = random.sample(user_logs, k=n)
        return random_logs
    except ValueError:
        return "Invalid argument - provided n is greater than user's log list size"

# Funcion that returns average time duration and standard deviation of time duration
def get_average_and_standard_deviation(logs):
    
    # Prepare list of timestamps but in a datetime format
    timestamps = [datetime.strptime(log['timestamp'], '%b %d %H:%M:%S') for log in logs]
    # Prepare list of duration time
    durations = [(timestamps[i+1] - timestamps[i]).total_seconds() for i in range(len(logs)-1)]
    
    # Calculate average time and standard deviation
    mean = statistics.mean(durations)
    dev = statistics.stdev(durations)
    # average = sum(durations) / len(durations)
    # deviation = (sum((duration - average) * 2 for duration in durations) / len(durations)) ** 0.5
    return mean, dev

# Function that returns average time duration and standard deviation of time duration for each user
def get_average_and_standard_deviation_for_users(logs):
    # Prepare logs and users list
    users_list = prepare_users_list(logs)
    
    # Prepare list of timestamps but in a datetime format for each user
    users_dictionary = {}
    for user in users_list:
        timestamps = [datetime.strptime(log['timestamp'], '%b %d %H:%M:%S') for log in logs if user in log['message']]
        durations = [(timestamps[i+1] - timestamps[i]).total_seconds() for i in range(len(timestamps)-1)]
        mean = statistics.mean(durations)
        dev = statistics.stdev(durations)
        users_dictionary[user] = (mean, dev)
        
    return users_dictionary
        

# Function that returns user with most logs and user with least logs
def get_most_and_least_logs_users(logs):
    # Prepare logs and users list
    users_list = prepare_users_list(logs)
    
    # Count logs for each user
    users_logs_count = []
    for user in users_list:
        users_logs_count.append((user, users_list.count(user)))
    
    # Sort list by number of logs
    users_logs_count.sort(key=lambda x: x[1])
    
    # Return user with most logs and user with least logs
    return users_logs_count[0], users_logs_count[-1]

# if _name_ == "_main_":
#     print(get_random_logs_from_random_user(sys.argv[1], sys.argv[2]))
#     print("User with least and most logs: ", get_most_and_least_logs_users(sys.argv[1]))
#     print(get_average_and_standard_deviation(sys.argv[1]))
#     print(get_average_and_standard_deviation_for_users(sys.argv[1]))