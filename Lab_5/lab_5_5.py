import argparse
import logging

from lab_5_1 import readLogs, parseLogs, parseMessages, printLogs
from lab_5_2 import parse_ssh_log, get_ipv4s_from_log, get_user_from_log, get_message_type
from lab_5_3 import loggingConfig
from lab_5_4 import get_random_logs_from_random_user, get_average_and_standard_deviation, get_average_and_standard_deviation_for_users, get_most_and_least_logs_users

desc = "#---------------------------------------------#" + "\n" + "| CLI designed for list 5 exercises |" + "\n" + "#---------------------------------------------#"
# parser = argparse.ArgumentParser(description='CLI designed for list 5 exercises')
parser = argparse.ArgumentParser(description=desc)

parser.add_argument('filePath', help='Path to the file with ssh logs')
parser.add_argument('-m', '--min_level', help='Set min level for logging', choices=['debug', 'info', 'warning', 'error', 'critical', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='DEBUG')
parser.add_argument('-sh', '--show_logs', action='store_true', help='Print logs')
parser.add_argument('-t', '--top', type=int, help='Number of printed lines from the top of the file')
parser.add_argument('-cl', '--clear', action='store_true', help='Clear the terminal after reading the file and before printing the result of the exercise execution')

subparsers = parser.add_subparsers(title='Exercises', dest='ex')

# subparser for Exercise 2b
parser_2_b = subparsers.add_parser('2b', help='Exercise 2b - get ipv4s from log')
parser_2_b.add_argument('--index', type=int, required=True, help='Index of log')
parser_2_b.set_defaults(func=get_ipv4s_from_log)

# subparser for Exercise 2c
parser_2_c = subparsers.add_parser('2c', help='Exercise 2c - get user from log')
parser_2_c.add_argument('--index', type=int, required=True, help='Index of log')
parser_2_c.set_defaults(func=get_user_from_log)

# subparser for Exercise 2d
parser_2_d = subparsers.add_parser('2d', help='Exercise 2d - get message type')
parser_2_d.add_argument('--index', type=int, required=True, help='Index of log')
parser_2_d.set_defaults(func2d=get_message_type)

# subparser_4 = parser.add_subparsers(title='Exercise 4', dest='ex_4')

# subparser for Exercise 4a
parser_4_a = subparsers.add_parser('4a', help='Exercise 4a - n random logs of related to the random user')
parser_4_a.add_argument('-n', '--number', type=int, required=True, help='number of logs to be drawn')
parser_4_a.set_defaults(func1=get_random_logs_from_random_user)

# subparsers for Exercise 4b
parser_4_b_i = subparsers.add_parser('4b_i', help='Exercise 4b_i - mean and standard deviation of ssh connection duration. Statistics related to the whole file')
parser_4_b_i.set_defaults(func2=get_average_and_standard_deviation)

parser_4_b_ii = subparsers.add_parser('4b_ii', help='Exercise 4b_ii - mean and standard deviation of ssh connection duration. Statistics grouped by every user')
parser_4_b_ii.set_defaults(func2=get_average_and_standard_deviation_for_users)

# subparser for Exercise 4c
parser_4_c = subparsers.add_parser('4c', help='Exercise 4c - most and least frequently logged users')
parser_4_c.set_defaults(func2=get_most_and_least_logs_users)

# parsing the arguments
args = parser.parse_args()

if hasattr(args, 'func') or hasattr(args, 'func2d') or hasattr(args, 'func1') or hasattr(args, 'func2') or args.show_logs or (args.top is not None):
    logger = loggingConfig(args.min_level.upper())
    logs = readLogs(args.filePath, parse_ssh_log, logger)
    if args.clear:
        for i in range(50):
            print('')
    print()
    print('Result:')
    if args.show_logs:
        printLogs(logs)
    elif (args.top is not None):
        printLogs(logs, number=args.top)
    elif hasattr(args, 'func'):
        print(args.func(logs[args.index-1]))
    elif hasattr(args, 'func2d'):
        print(args.func2d(logs[args.index-1]['message']))
    elif hasattr(args, 'func1'):
        print(args.func1(logs, args.number))
    else:
        print(args.func2(logs))
else:
    parser.print_help()
