import logging
from abc import ABC, abstractmethod
from typing import NoReturn

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class Vehicle(ABC):

    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass