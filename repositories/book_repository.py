from db.run_sql import run_sql


from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository


def save(book):
    sql = "INSERT INTO books (book_title, author_id) VALUES (%s, %s) RETURNING *"
    values = [book.book_title, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    all_books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repository.select_1_by_id(row['author_id'])
        book = Book(row['book_title'], author, row['id'])
        all_books.append(book)
    return all_books

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)