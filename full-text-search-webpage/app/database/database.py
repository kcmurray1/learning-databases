"""A generic database used to store Youtube video information"""
from .search_statements import SqlStatements
import sqlite3

class BookDatabase:

    def __init__(self, database_path):
        self.database_path = database_path
      

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
        
    def insert_book(self, values):
        try:
            self.cursor.execute(SqlStatements.INSERT_BOOK, values)
        except sqlite3.IntegrityError:
            pass
    
    # def insert_book(self, columns, values):
    #     try:
    #         (AuthorID, Price, Title, Category, Month, Year, Description) = values
            
    #         self.cursor.execute(SqlStatements.INSERT_QUERY.format(Table="Books", Columns=columns, Values=values))
    #     except (sqlite3.IntegrityError):
    #         print("ERROR")
    #         pass    

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

    def find(self, channel_id, phrase):
        """Find channels that have videos containing the phrase
        Args: 
            channel_id: int representing a channel
            phrase: a str for the phrase to find in the database
        Returns: a list of tuple(video title, url) pertinent to the phrase otherwise returns
            None
        """
        res = self.cursor.execute(SqlStatements.RETRIEVE_CHANNEL_PHRASE, (channel_id, phrase))

        return res.fetchall()
        