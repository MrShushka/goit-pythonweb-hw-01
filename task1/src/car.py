import logging
from vehicle import Vehicle 

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class Car(Vehicle):

    def start_engine(self) -> None:
        """Запускає двигун автомоremoveбіля."""
        logging.info(f"{self.make} {self.model}: Двигун запущено")