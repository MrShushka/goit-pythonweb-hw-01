import logging
from typing import List
from book import Book  
from library_interface import LibraryInterface  

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class Library(LibraryInterface):

    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logging.info(f"Додано книгу: {book.title}")

    def remove_book(self, title: str) -> None:
        original_count = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        if len(self.books) < original_count:
            logging.info(f"Видалено книгу з назвою: {title}")
        else:
            logging.warning(f"Книгу з назвою '{title}' не знайдено.")

    def get_books(self) -> List[Book]:
        return self.books