import logging
from vehicle import Vehicle 

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class Motorcycle(Vehicle):

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Мотор заведено")
