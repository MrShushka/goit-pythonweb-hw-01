import logging
from vehicle_factory import VehicleFactory 
from car import Car 
from motorcycle import Motorcycle 

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class EUVehicleFactory(VehicleFactory):

    def create_car(self, make: str, model: str) -> Car:

        logging.info(f"Створення Car для ЄС: {make} {model} (EU Spec)")
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:

        logging.info(f"Створення Motorcycle для ЄС: {make} {model} (EU Spec)")
        return Motorcycle(make, f"{model} (EU Spec)")

