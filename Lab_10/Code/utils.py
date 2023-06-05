import os
import logging
import sys

# !!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!! #
# Please set a valid path to the directory, where all data has been downloaded
data_dir_path = 'C:\\Users\\Kris\\Documents\\Studia\\Semestr_IV\\Jezyki_skryptowe_L\\Laboratoria\\Lab_10\\Data\\'
db_dir_path = 'C:\\Users\\Kris\\Documents\\Studia\\Semestr_IV\\Jezyki_skryptowe_L\\Laboratoria\\Lab_10\\DBs\\'
log_level = 'WARNING'
# --------------------------------------- #

os.environ['DATA_PATH'] = data_dir_path
os.environ['LOG_LEVEL'] = log_level
os.environ['DB_PATH'] = db_dir_path

def set_logger(logger: logging.Logger, log_level: str):
    num_level = getattr(logging, log_level)
    logger.setLevel(level=num_level)

    stdout_handler = logging.StreamHandler(sys.stdout)
    formatter_stdout = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stdout_handler.setFormatter(formatter_stdout)

    logger.addHandler(stdout_handler)


def print_loading_progress(number_done: int, number_all: int):
    print('\r', f"Number of added rows: {number_done}/{number_all}", end = '')
    # print(f"Number of added rows: {number_done}/{number_all}")
    sys.stdout.flush()