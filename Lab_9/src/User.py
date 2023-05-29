import sys
sys.path.append("C:\\Users\\Kris\\Documents\\Studia\\Semestr_IV\\Jezyki_skryptowe_L\\Laboratoria\\Lab_9")

import re
from src.Journal import SSHLogJournal
from src.parse_log import parse_ssh_log
from src.LogEntries import *
from src.Journal import SSHLogJournal
from src.Utils import *

class SSHUser:
    def __init__(self, username, last_login_date):
        self.username = username
        self.last_login_date = last_login_date
        
    def validate(self):
        # print("Validating user: ", self.username)
        pattern = r'^[a-z_][a-z0-9_-]{0,31}$'
        match = re.match(pattern, self.username)
        if match:
            return True
        return False
    
if __name__ == '__main__':
    journal = SSHLogJournal()
    file_path = 'C:\\Users\\Kris\\Documents\\Studia\\Semestr_IV\\Jezyki_skryptowe_L\\Laboratoria\\Lab_9\\logs.txt'
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            journal.append(line)
    users = []
    for entry in journal:
        user = SSHUser(entry.host, entry.timestamp)
        flag = True
        i = 0
        while (flag and i < len(users)):
            u = users[i]
            if u.username == user.username:
                u.last_login_date = user.last_login_date
                flag = False
            i+=1
        if (user.username != None and flag == True):
            users.append(user)
            
    list = journal.logList + users
    for sth in list:
        validation = sth.validate()
        if not validation:
            print(f'False, {sth}')
    
    
        