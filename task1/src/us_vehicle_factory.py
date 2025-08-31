import logging
from vehicle_factory import VehicleFactory 
from car import Car 
from motorcycle import Motorcycle 

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class USVehicleFactory(VehicleFactory):

    def create_car(self, make: str, model: str) -> Car:
        logging.info(f"Створення Car для США: {make} {model} (US Spec)")
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        logging.info(f"Створення Motorcycle для США: {make} {model} (US Spec)")
        return Motorcycle(make, f"{model} (US Spec)")
