import logging
from book import Book  
from library_interface import LibraryInterface  
from typing import List, Dict, Any, Optional

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class LibraryManager:

    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        try:
            book = Book(title=title, author=author, year=int(year))
            self.library.add_book(book)
        except ValueError:
            logging.error("Рік повинен бути цілим числом.")

    def remove_book(self, title: str) -> None:

        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            logging.info("У бібліотеці немає книг.")
            return

        for book in books:
            logging.info(
                f"Назва: {book.title}, Автор: {book.author}, Рік: {book.year}"
            )