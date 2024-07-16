"""Common Database queries used by the program"""
class SqlStatements():
    ALL = "SELECT * FROM Channels"
    INSERT_CHANNEL = "INSERT INTO Channels (Handle, Name) VALUES (?, ?)"
    INSERT_VIDEO = "INSERT INTO Videos (ChannelID, Transcript, Title, Url) VALUES (?, ?, ?, ?)"
    RETRIEVE_CHANNEL = "SELECT ChannelID FROM Channels where Handle = ? OR Name LIKE ?"
    RETRIEVE_CHANNEL_PHRASE = "SELECT Title, URL FROM Videos where ChannelID = ? AND Transcript LIKE ?"