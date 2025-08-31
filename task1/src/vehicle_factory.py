from abc import ABC, abstractmethod
from car import Car  
from motorcycle import Motorcycle  

class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:

        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass

