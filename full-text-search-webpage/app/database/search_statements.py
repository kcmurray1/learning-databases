"""Common Database queries used by the program"""
class SqlStatements():
    INSERT_AUTHOR = "INSERT INTO Authors (First_name, Last_name) VALUES (?, ?)"
    INSERT_BOOK = "INSERT INTO Books (price, title, month, year, description) VALUES (?, ?, ?, ?, ?)"
    INSERT_BOOK_AUTHOR = "INSERT INTO BookAuthors (author_id, book_id) VALUES (?, ?)"

    RETRIEVE_AUTHOR = "SELECT author_id FROM Authors WHERE first_name = ? AND last_name = ?"
    
    RETRIEVE_BOOK_WITH_LIMIT = """SELECT GROUP_CONCAT(a.first_name || ' ' || a.last_name, ', ') AS authors, b.price, b.title, b.month, b.year, b.description 
    FROM Books b 
    JOIN BookAuthors ba ON b.book_id = ba.book_id
    JOIN Authors a ON ba.author_id = a.author_id
    GROUP BY b.book_id
    LIMIT ? OFFSET ?"""

    RETRIEVE_BOOK_WITH_FILTER = """SELECT GROUP_CONCAT(a.first_name || ' ' || a.last_name, ', ') AS authors, b.price, b.title, b.month, b.year, b.description 
    FROM Books b 
    JOIN BookAuthors ba ON b.book_id = ba.book_id
    JOIN Authors a ON ba.author_id = a.author_id
    WHERE {Filter}
    GROUP BY b.book_id"""


    INSERT_CATEGORY = "INSERT INTO Categories (name) VALUES (?)"

    INSERT_BOOK_CATEGORIES = "INSERT INTO BookCategories (book_id, category_id) VALUES (?, ?)"

    RETRIEVE_CATEGORY = "SELECT name FROM Categories WHERE name = ?"

    RETRIEVE_CATEGORIES_ALL = "SELECT * FROM Categories"

    TEMPLATE_FILTER_CATEGORY = "OR c.category_id = ? "
    TEMPLATE_FILTER_CATEGORY_START = "c.category_id = ? " 
    TEMPLATE_FILTER_SEARCH = """SELECT GROUP_CONCAT(a.first_name || ' ' || a.last_name, ', ') AS authors, b.price, b.title, b.month, b.year, b.description 
FROM Books b 
JOIN BookAuthors ba ON b.book_id = ba.book_id
JOIN Authors a ON ba.author_id = a.author_id
JOIN BookCategories bc ON bc.book_id = b.book_id
JOIN Categories c ON c.category_id = bc.category_id
WHERE {Filter}
GROUP BY b.book_id"""