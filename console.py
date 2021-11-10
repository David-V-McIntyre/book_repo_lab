from models.author import Author
from models.book import Book

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

# author_1 = Author("Stephen King")
# author_repository.save(author_1)

# book_1 = Book("IT", author_1)
# book_repository.save(book_1)

# author_2 = Author("George Orwell")
# author_repository.save(author_2)

# book_2 = Book("1984", author_2)
# book_repository.save(book_2)

# author_3 = Author("Brett Easton Ellis")
# author_repository.save(author_3)

# book_3 = Book("American Psycho", author_3)
# book_repository.save(book_3)

def print_all():
    results = book_repository.select_all()
    for row in results:
        print(row)

print_all()