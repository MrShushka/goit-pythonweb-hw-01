import logging
from vehicle_factory import VehicleFactory # Імпорт з vehicle_factory.py
from us_vehicle_factory import USVehicleFactory # Імпорт з us_vehicle_factory.py
from eu_vehicle_factory import EUVehicleFactory # Імпорт з eu_vehicle_factory.py
from car import Car # Імпорт з car.py (для типізації)
from motorcycle import Motorcycle # Імпорт з motorcycle.py (для типізації)


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main() -> None:
    logging.info("--- Створення транспортних засобів для США ---")
    us_factory: VehicleFactory = USVehicleFactory()

    us_car: Car = us_factory.create_car("Ford", "Mustang")
    us_car.start_engine()

    us_motorcycle: Motorcycle = us_factory.create_motorcycle("Indian", "Scout")
    us_motorcycle.start_engine()

    logging.info("\n--- Створення транспортних засобів для ЄС ---")
    eu_factory: VehicleFactory = EUVehicleFactory()

    eu_car: Car = eu_factory.create_car("Volkswagen", "Golf")
    eu_car.start_engine()

    eu_motorcycle: Motorcycle = eu_factory.create_motorcycle("BMW", "R 1250 GS")
    eu_motorcycle.start_engine()


if __name__ == "__main__":

    main()


