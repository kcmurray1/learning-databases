"""Common Database queries used by the program"""
class SqlStatements():
    INSERT_VIDEO = "INSERT INTO Videos (ChannelID, Transcript, Title, Url) VALUES (?, ?, ?, ?)"
    RETRIEVE_CHANNEL = "SELECT ChannelID FROM Channels where Handle = ? OR Name LIKE ?"
    RETRIEVE_CHANNEL_PHRASE = "SELECT Title, URL FROM Videos where ChannelID = ? AND Transcript LIKE ?"

    INSERT_QUERY = "INSERT INTO {Table} {Columns} VALUES {Values};"
    INSERT_DEBUG_QUERY = "INSERT INTO Books (AuthorID, Price, Title, Category, Month, Year, Description) VALUES (?, ?, ?, ?, ?, ?, ?)"

    INSERT_AUTHOR = "INSERT INTO Authors (First_name, Last_name) VALUES (?, ?)"
    INSERT_BOOK = "INSERT INTO Books (AuthorID, Price, Title, Category, Month, Year, Description) VALUES (?, ?, ?, ?, ?, ?, ?)"

    RETRIEVE_AUTHOR = "SELECT ID FROM Authors WHERE First_name = ? AND Last_name = ?"
    RETRIEVE_BOOK_WITH_LIMIT = "SELECT Price, Title, Category, Month, Year, Description FROM Books LIMIT ? OFFSET ?"