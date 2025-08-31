import logging
from library import Library  
from library_manager import LibraryManager  

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    logging.info("--- Ласкаво просимо до Бібліотеки ---")

    while True:
        command = input("Введіть команду (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Введіть назву книги: ").strip()
                author = input("Введіть автора книги: ").strip()
                year = input("Введіть рік видання: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Введіть назву книги для видалення: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.warning("Недійсна команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()