from db.run_sql import run_sql

from models.author import Author

def save(author):
    sql = "INSERT INTO authors (author_name) VALUES (%s) RETURNING *"
    values = [author.author_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

