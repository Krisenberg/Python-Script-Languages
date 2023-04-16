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
parser.add_argument('-m', '--min_level', help='Min level for logging', choices=['debug', 'info', 'warning', 'error', 'critical', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='DEBUG')
parser.add_argument('-sh', '--show_logs', action='store_true', help='Print logs')
parser.add_argument('-t', '--top', type=int, help='Number of printed lines from the top of the file')

subparser_2 = parser.add_subparsers(title='Exercise 2', dest='ex_2')

# subparser for Exercise 2b
parser_2_b = subparser_2.add_parser('2b', help='Exercise 2b - get ipv4s from log')
parser_2_b.add_argument('--index', type=int, required=True, help='Index of log')
parser_2_b.set_defaults(func=get_ipv4s_from_log)

# subparser for Exercise 2c
parser_2_c = subparser_2.add_parser('2c', help='Exercise 2c - get user from log')
parser_2_c.add_argument('--index', type=int, required=True, help='Index of log')
parser_2_c.set_defaults(func=get_user_from_log)

# subparser for Exercise 2d
parser_2_d = subparser_2.add_parser('2d', help='Exercise 2d - get message type')
parser_2_d.add_argument('--index', type=int, required=True, help='Index of log')
parser_2_d.set_defaults(func=get_message_type)

subparser_4 = parser.add_subparsers(title='Exercise 4', dest='ex_4')

# subparser for Exercise 4a
parser_4_a = subparser_4.add_parser('4a', help='Exercise 4a - n random logs of related to the random user')
parser_4_a.add_argument('-n', '--number', type=int, required=True, help='number of logs to be drawn')
parser_4_a.set_defaults(func=get_random_logs_from_random_user)

# subparsers for Exercise 4b
parser_4_b_i = subparser_4.add_parser('4b_i', help='Exercise 4b_i - mean and standard deviation of ssh connection duration. Statistics related to the whole file')
parser_4_b_i.set_defaults(func=get_average_and_standard_deviation)

parser_4_b_ii = subparser_4.add_parser('4b_ii', help='Exercise 4b_ii - mean and standard deviation of ssh connection duration. Statistics grouped by every user')
parser_4_b_ii.set_defaults(func=get_average_and_standard_deviation_for_users)

# subparser for Exercise 4c
parser_4_c = subparser_4.add_parser('4c', help='Exercise 4c - most and least frequently logged users')
parser_4_c.set_defaults(func=get_most_and_least_logs_users)

# parsowanie argumentów
args = parser.parse_args()
logger = loggingConfig(args.min_level.upper())
logs = readLogs(args.filePath, parse_ssh_log, logger)

executedFlag = False

if args.show_logs:
    printLogs(logs)
    executedFlag = True

if args.top:
    printLogs(logs, args.top)
    executedFlag = True

if hasattr(args, 'func'):
    if args.index:
        print(args.func(logs[args.index-1]))
    elif args.number:
        print(args.func(logs, args.number))
    else:
        print(args.func(logs))
else:
    parser.print_help()
#     executedFlag = True

# if hasattr(args, 'func_4a'):
#     print(args.func_4a(logs, args.n))
#     executedFlag = True

# if hasattr(args, 'func_4b_i'):
#     print(args.func_4b_i(logs))
#     executedFlag = True

# if hasattr(args, 'func_4b_ii'):
#     print(args.func_4b_ii(logs))
#     executedFlag = True

# if hasattr(args, 'func_4c'):
#     print(args.func_4c(logs))
#     executedFlag = True

# if not(executedFlag):
#     parser.print_help()
