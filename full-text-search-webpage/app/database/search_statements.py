"""Common Database queries used by the program"""
class SqlStatements():
    INSERT_AUTHOR = "INSERT INTO Authors (First_name, Last_name) VALUES (?, ?)"
    INSERT_BOOK = "INSERT INTO Books (price, title, month, year, description) VALUES (?, ?, ?, ?, ?)"
    INSERT_BOOK_AUTHOR = "INSERT INTO BookAuthors (author_id, book_id) VALUES (?, ?)"

    RETRIEVE_AUTHOR = "SELECT author_id FROM Authors WHERE first_name = ? AND last_name = ?"
    
    RETRIEVE_BOOK_WITH_LIMIT = "SELECT a.first_name, a.last_name, b.price, b.title, b.month, b.year, b.description FROM Books b JOIN BookAuthors ba ON b.book_id = ba.book_id JOIN Authors a ON ba.author_id = a.author_id LIMIT ? OFFSET ?"
    BOOK_AUTHOR = "SELECT * FROM BookAuthors"
    idk = "SELECT a.first_name, a.last_name, b.price, b.title, b.month, b.year, b.description FROM Books b JOIN BookAuthors ba ON b.book_id = ba.book_id JOIN Authors a ON ba.author_id = a.author_id LIMIT ? OFFSET ?"