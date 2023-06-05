import Models
from sqlalchemy import create_engine
from sqlalchemy import Engine
import sys
import os

def create_db(db_name: str, log: bool) -> Engine:
    db_dir_path = (os.environ.get('DB_PATH')) if os.environ.get('DB_PATH', '') != '' else None
    if db_dir_path is not None:
        if not os.path.isdir(db_dir_path):
            os.mkdir(db_dir_path)
    db_path = db_dir_path + db_name + '.db'
    engine = create_engine(f"sqlite:///{db_path}", echo=False)
    if log:
        engine.echo = True
    Models.Base.metadata.create_all(engine)
    return engine

if __name__=='__name__':
    db_name = sys.argv[1] if len(sys.argv) > 1 else "rentals"
    create_db(db_name)