import Models
from sqlalchemy import create_engine
import sys

def create_db(db_name: str) -> None:
    engine = create_engine(f"sqlite:///{db_name}.db", echo=True)
    Models.Base.metadata.create_all(engine)

if __name__=='__name__':
    db_name = sys.argv[1] if len(sys.argv) > 1 else "rentals"
    create_db(db_name)