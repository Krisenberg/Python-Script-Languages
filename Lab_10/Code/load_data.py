import os
import pandas as pd
from csv import DictReader
from sqlalchemy import create_engine


def load_file(data_dir_path: str, file_name: str, db_name: str):

    db_engine = create_engine(f"sqlite:///{db_name}.db", echo=True)

    file_path = data_dir_path + file_name
    headers = ['rental_id', 'bike_number', 'start_time', 'end_time', 'rental_station'
               'return_station', 'duration']
    with open(file_path, 'r') as f:
        data = DictReader(f, fieldnames=headers)


data_dir_path = (os.environ.get('DATA_PATH')) if os.environ.get('DATA_PATH', '') != '' else None