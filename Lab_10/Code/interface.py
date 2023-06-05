import sys
import os
import utils
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox
from PySide6.QtCore import Qt
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker
from Models import Base, Rental, Station

db_name = 'rentals'
db_path = os.environ.get('DB_PATH') + db_name + '.db'
# Connect to the database
engine = create_engine(f"sqlite:///{db_path}")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Adjusting the window
        self.setWindowTitle("Analiza stacji rowerowych")
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        # Specyfing the layout (vertical)
        layout = QVBoxLayout(self.central_widget)
        
        # Adding a widget to chose the station
        self.station_label = QLabel("Wybierz stację nr 1:")
        layout.addWidget(self.station_label)

        # Adding a combo box to chose the station with list of all stations
        self.stations = QComboBox()
        self.add_stations(self.stations)
        layout.addWidget(self.stations)

        # Button for ex 3a
        self.rental_duration_button = QPushButton("Sredni czas trwania przejazdu rozpoczynanego na stacji nr 1")
        self.rental_duration_button.clicked.connect(self.avg_rental)
        layout.addWidget(self.rental_duration_button)

        # Button for ex 3b
        self.return_duration_button = QPushButton("Średni czas trwania przejazdu kończonego na stacji nr 1")
        self.return_duration_button.clicked.connect(self.avg_return)
        layout.addWidget(self.return_duration_button)

        # Button for ex 3c
        self.bikes_count_button = QPushButton("Liczba różnych rowerów parkowanych na stacji nr 1")
        self.bikes_count_button.clicked.connect(self.calculate_bikes_count)
        layout.addWidget(self.bikes_count_button)
        
        # Adding a widget to chose the station
        self.station_label = QLabel("Wybierz stację nr 2:")
        layout.addWidget(self.station_label)

        # Adding a combo box to chose the end station with list of all stations
        self.stations_end = QComboBox()
        self.add_stations(self.stations_end)
        layout.addWidget(self.stations_end)
        
        # Button for ex 3d
        self.trip_count_button = QPushButton("Liczba przejazdów ze stacji nr 1 do stacji nr 2")
        self.trip_count_button.clicked.connect(self.calculate_trip_count)
        layout.addWidget(self.trip_count_button)

    def add_stations(self, where):
        stations = session.query(Station).all()
        for station in stations:
            where.addItem(station.station_name, station.station_id)

    def avg_rental(self):
        station_id = self.stations.currentData()
        station_name = self.stations.currentText()

        if station_id is None:
            QMessageBox.warning(self, "Błąd", "Nie wybrano stacji.")
            return

        selects = select(func.avg(Rental.duration)).where(Rental.rental_station_id == station_id)
        avg_duration = session.execute(selects).scalar()

        message = f"Średni czas trwania przejazdu rozpoczynanego na stacji {station_name}: {avg_duration:.2f}"

        QMessageBox.information(self, "Wyniki", message)

    def avg_return(self):
        station_id = self.stations.currentData()
        station_name = self.stations.currentText()

        if station_id is None:
            QMessageBox.warning(self, "Błąd", "Nie wybrano stacji.")
            return

        selects = select(func.avg(Rental.duration)).where(Rental.return_station_id == station_id)
        avg_duration = session.execute(selects).scalar()

        message = f"Średni czas trwania przejazdu kończonego na stacji {station_name}: {avg_duration:.2f}"

        QMessageBox.information(self, "Wyniki", message)

    def calculate_bikes_count(self):
        station_id = self.stations.currentData()
        station_name = self.stations.currentText()

        if station_id is None:
            QMessageBox.warning(self, "Błąd", "Nie wybrano stacji.")
            return

        selects = select(func.count(Rental.bike_number.distinct())).where(Rental.rental_station_id == station_id or Rental.return_station_id == station_id)
        bikes_count = session.execute(selects).scalar()

        message = f"Liczba różnych rowerów parkowanych na stacji {station_name}: {bikes_count}"

        QMessageBox.information(self, "Wyniki", message)
        
    def calculate_trip_count(self):
        start_station_id = self.stations.currentData()
        end_station_id = self.stations_end.currentData()
        start_station_name = self.stations.currentText()
        end_station_name = self.stations_end.currentText()

        if start_station_id is None or end_station_id is None:
            QMessageBox.warning(self, "Błąd", "Nie wybrano odpowiednich stacji.")
            return

        selects = select(func.count()).where(Rental.rental_station_id == start_station_id and Rental.return_station_id == end_station_id)
        trip_count = session.execute(selects).scalar()

        if start_station_id == end_station_id:
            QMessageBox.warning(self, "Błąd", "Wybrano dwie takie same stacje.")
            return

        message = f"Liczba przejazdów z(e) stacji {start_station_name} do stacji {end_station_name}: {trip_count}"

        QMessageBox.information(self, "Wyniki", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())