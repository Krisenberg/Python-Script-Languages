#import load_data
from load_data import *

def check_file_existence(data_dir_path: str):
    present_files_names = {entry.name for entry in os.scandir(data_dir_path)}
    for month in range(1,13):
        month_str = f'{month}' if month>=10 else f'0{month}'
        file_name = f"historia_przejazdow_2021-{month_str}.csv"
        if file_name not in present_files_names:
            return False
    return True

def load_2021(data_dir_path: str, db_engine: Engine):
    for month in range(1,13):
        month_str = f'{month}' if month>=10 else f'0{month}'
        file_name = f"historia_przejazdow_2021-{month_str}.csv"
        load_file(data_dir_path, file_name, db_engine)

if __name__ == "__main__":

    if len(sys.argv) >= 2:
        db_name = sys.argv[1]
    else:
        raise ValueError("Not enough args have been provided")
    
    data_dir_path = (os.environ.get('DATA_PATH')) if os.environ.get('DATA_PATH', '') != '' else None
    
    # check if DATA_PATH is set correctly
    if data_dir_path is not None:
        if check_file_existence(data_dir_path):
            log_level = (os.environ.get('LOG_LEVEL')) if os.environ.get('LOG_LEVEL', '') != '' else None
            if log_level is None:
                log_level = 'WARNING'
            app.set_logger(logging.getLogger('sqlalchemy.engine'), log_level)
            db_engine = create_engine(f"sqlite:///{db_name}.db", echo=True)
            Base.metadata.create_all(db_engine)
            load_2021(data_dir_path, db_engine)          
        else:
            raise FileNotFoundError("No such file in the DATA_PATH directory")
    else:
        print('DATA_PATH variable is not set')
