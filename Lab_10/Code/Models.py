from typing import List, Optional
from sqlalchemy import ForeignKey, String, Float, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Rental(Base):

    __tablename__ = "rentals"

    rental_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    bike_number: Mapped[int] = mapped_column(ForeignKey('bikes.bike_id'))
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
    duration: Mapped[int] = mapped_column(Integer)
    rental_station_id: Mapped[int] = mapped_column(ForeignKey('stations.station_id'))
    return_station_id: Mapped[int] = mapped_column(ForeignKey('stations.station_id'))

    rental_station: Mapped['Station'] = relationship(foreign_keys=[rental_station_id],
                                                     back_populates='rentals_start')
    return_station: Mapped['Station'] = relationship(foreign_keys=[return_station_id],
                                                     back_populates='rentals_end')
    bike: Mapped['Bike'] = relationship(foreign_keys=[bike_number],
                                        back_populates='bike_rentals')

    def __repr__(self) -> str:
        return f"Rental(UID={self.rental_id!r}, bike_number={self.bike_number!r}, " \
               f"start_time={self.start_time!r}, end_time={self.end_time!r}, " \
               f"rental_station={self.rental_station!r}, return_station={self.return_station!r})"


class Bike(Base):
    
    __tablename__ = "bikes"

    bike_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)

    bike_rentals: Mapped[List['Rental']] = relationship(back_populates='bike')
    
    def __repr__(self):
        return f"Bike(bike_id={self.bike_id!r})"

class Station(Base):
    __tablename__ = "stations"

    station_id: Mapped[int] = mapped_column(primary_key=True)
    station_name: Mapped[str] = mapped_column(String(30))

    rentals_start: Mapped[List['Rental']] = relationship(back_populates='rental_station',
                                                            foreign_keys="[Rental.rental_station_id]")
    rentals_end: Mapped[List['Rental']] = relationship(back_populates='return_station',
                                                            foreign_keys="[Rental.return_station_id]")

    def __repr__(self):
        return f"Station(station_id={self.station_id!r}, station_name={self.station_name!r})"