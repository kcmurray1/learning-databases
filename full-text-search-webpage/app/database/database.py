"""A generic database used to store Youtube video information"""
import sqlite3
from .search_statements import SqlStatements

class BookDatabase:

    def __init__(self, database_path):
        self.database_path = database_path
        self.book_offset = 0
        self.book_offset_size = 10
        self.query = None
      

    def __enter__(self):
        """Allow support for the 'with' keyword"""
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        return self
    
    def __exit__(self, exc_type, exc_val, traceback):
        """Used at the end of 'with' block and handle exceptions that occur"""
        self.connection.commit()
        self.connection.close()

    def reset(self):
        self.book_offset = 0
        self.query = None
        
    def insert_book(self, values):
        try:
            self.cursor.execute(SqlStatements.INSERT_BOOK, values)
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            pass
    
    def insert_book_author(self, author_id, book_id):
        try:
            self.cursor.execute(SqlStatements.INSERT_BOOK_AUTHOR, (author_id, book_id))
        except sqlite3.IntegrityError:
            pass
    
    def insert_author(self, author: tuple):
        """Adds author to database
        Args:
            author: a tuple (first_name, last_name)
        Returns:
            The author's ID in the database
        """
        # Check if author already exists
        res = self.cursor.execute(SqlStatements.RETRIEVE_AUTHOR, author)
        res = res.fetchone()
        # Add new other to database
        if not res:
            self.cursor.execute(SqlStatements.INSERT_AUTHOR, author)
            res = self.cursor.execute(SqlStatements.RETRIEVE_AUTHOR, author).fetchone()
        # Return AuthorID
        return res[0]

    def insert_category(self, category):
        print(category)
         # Check if category already exists
        res = self.cursor.execute(SqlStatements.RETRIEVE_CATEGORY, (category,))
        res = res.fetchone()
        if res:
            return res[0]
        # Add new category to database
        self.cursor.execute(SqlStatements.INSERT_CATEGORY, (category,))
        return self.cursor.lastrowid

    def insert_book_category(self, book_id, category_id):
        try:
            print(book_id, category_id)
            self.cursor.execute(SqlStatements.INSERT_BOOK_CATEGORIES, (book_id, category_id))
        except sqlite3.IntegrityError:
            pass

    def get_books(self):
        # Return 10 books from database
        res = []
        if self.query:
                res = self.cursor.execute(self.query)
        else:
            res = self.cursor.execute(SqlStatements.RETRIEVE_BOOK_WITH_LIMIT, (self.book_offset_size, self.book_offset))
            self.book_offset += self.book_offset_size
        res = res.fetchall()
        
        return res

    def get_categories(self):
        res = self.cursor.execute(SqlStatements.RETRIEVE_CATEGORIES_ALL)
        res = res.fetchall()

        return res
    
    def execute_query(self, search_term, categories):
        # Do nothing if there is nothing to search for
        if not search_term and not categories:
            return
        
        query = SqlStatements.TEMPLATE_FULL_TEST_SEARCH

        categories = categories[1:]
        filter = ""

        if search_term:
            filter += SqlStatements.TEMPLATE_AUTHORS_FTS.format(author=search_term)

        if categories:
            if filter:
                filter += " AND "
            filter += SqlStatements.TEMPLATE_CATEGORIES_FILTER.format(categories=tuple(categories) if len(categories) > 1 else f"({categories[0]})")
            query += SqlStatements.TEMPLATE_CATEGORIES_COUNT.format(len_categories=len(categories))

    
        query = query.format(Filter=filter)
        self.query = query
        

        

    # def execute_query(self, search_term, categories):
    #     if not search_term:
    #         categories = categories[1:]
        
    #     query = SqlStatements.TEMPLATE_FILTER_SEARCH
    #     filters = SqlStatements.TEMPLATE_FILTER_CATEGORY_START + SqlStatements.TEMPLATE_FILTER_CATEGORY * (len(categories) - 1)
    #     query = query.format(Filter=filters)
    #     print(query)
    #     self.query = (query, categories)
    #     # res = self.cursor.execute(query, categories)
    #     # print(res.fetchall())        