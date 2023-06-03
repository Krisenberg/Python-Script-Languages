import os
import sys
import pandas as pd
from csv import DictReader
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from Models import Rental, Bike, Station, Base
from typing import Dict
import app
from datetime import datetime
import logging

def try_to_add_object(obj, session):
    try:
        session.add(obj)
        session.commit()
    except IntegrityError:
        session.rollback()

def add_row(data: Dict[str, str], session: Session):

    try_to_add_object(Bike(bike_id=data['bike_number']), session)
    try_to_add_object(Station(station_name=data['rental_station']), session)
    try_to_add_object(Station(station_name=data['return_station']), session)

    rental_s_id = session.scalar(select(Station).where(Station.station_name == data['rental_station'])).station_id
    return_s_id = session.scalar(select(Station).where(Station.station_name == data['return_station'])).station_id
    rental = Rental(rental_id=data['rental_id'],
                    bike_number=data['bike_number'],
                    start_time=datetime.strptime(data['start_time'], "%Y-%m-%d %H:%M:%S"),
                    end_time=datetime.strptime(data['end_time'], "%Y-%m-%d %H:%M:%S"),
                    duration=data['duration'],
                    rental_station_id=rental_s_id, 
                    return_station_id=return_s_id)
    try_to_add_object(rental, session)


def load_file(data_dir_path: str, file_name: str, db_engine: Engine):

    file_path = data_dir_path + file_name
    headers = ['rental_id', 'bike_number', 'start_time', 'end_time', 'rental_station',
               'return_station', 'duration']
    with Session(db_engine) as session:
        number_of_rows = 0
        with open(file_path, encoding='utf-8') as f:
            data = DictReader(f, fieldnames=headers)
            number_of_rows = sum([1 for _ in data])
        with open(file_path, encoding='utf-8') as f:
            data = DictReader(f, fieldnames=headers)
            next(data)
            for i, row in enumerate(data):
               add_row(row, session)
               app.print_loading_progress(i+1, number_of_rows-1)

if __name__ == "__main__":

    if len(sys.argv) >= 3:
        file_name = sys.argv[1]
        db_name = sys.argv[2]
    else:
        raise ValueError("Not enough args have been provided")
    
    data_dir_path = (os.environ.get('DATA_PATH')) if os.environ.get('DATA_PATH', '') != '' else None
    print(data_dir_path)
    # check if DATA_PATH is set correctly
    if data_dir_path is not None:
        files_names = {file.name for file in os.scandir(data_dir_path)}
        if file_name not in files_names:
            raise FileNotFoundError("No such file in the DATA_PATH directory")
        
        log_level = (os.environ.get('LOG_LEVEL')) if os.environ.get('LOG_LEVEL', '') != '' else None
        if log_level is None:
            log_level = 'WARNING'
        app.set_logger(logging.getLogger('sqlalchemy.engine'), log_level)
        db_engine = create_engine(f"sqlite:///{db_name}.db", echo=False)
        Base.metadata.create_all(db_engine)
        load_file(data_dir_path, file_name, db_engine)
        
    else:
        print('DATA_PATH variable is not set')
