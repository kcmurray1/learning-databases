"""A generic database used to store Youtube video information"""
from .search_statements import SqlStatements
import sqlite3

class YoutubeDataBase:

    def __init__(self, database_path):
        self.database_path = database_path
      

    def __enter__(self):
        """Allow support for the 'with' keyword"""
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, traceback):
        """Used at the end of 'with' block and handle exceptions that occur"""
        self.connection.commit()
        self.connection.close()

    def get_channel(self, handle, name=None):
        """Retrieve data from the database
        Args:
            handle: a str representing the unique channel @<handle>
            name: a str representing the name of the channel
        Returns:
            an int representing the newly added channel id
        """
        # handles must have @ at the front
        if handle and handle[0] != '@':
            name = handle
            handle = None
        
        # Get channel id and update Channels table if channel not in database
        cur = self.cursor.execute(SqlStatements.RETRIEVE_CHANNEL, (handle, name))
        channel_id = cur.fetchone()

        if channel_id:
            return channel_id[0]
        return None

    def add_video(self, channel_id, transcript, title, url):
        try:
            self.cursor.execute(SqlStatements.INSERT_VIDEO, (channel_id, transcript, title, url))
        except sqlite3.IntegrityError:
            pass    

    def add_channel(self, handle, name=None):
        """Enter data for a channel
        Args:
            handle: a str representing the unique channel @<handle>
            name: a str representing the name of the channel
        Returns:
            an int representing the newly added channel id
        NOTE: channel handles are unique; whereas, names are not always unique.
        """
        try:
            self.cursor.execute(SqlStatements.INSERT_CHANNEL, (handle, name))
        except sqlite3.IntegrityError:
            pass
        cur = self.cursor.execute(SqlStatements.RETRIEVE_CHANNEL, (handle, name))
        return cur.fetchone()

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
        