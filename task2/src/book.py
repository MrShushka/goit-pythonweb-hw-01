import logging
from typing import NoReturn

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class Book:

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self) -> str:
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"
