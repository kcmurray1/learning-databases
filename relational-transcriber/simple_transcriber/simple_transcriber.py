"""A simple class to extract and store transcipts of youtube videos into a database"""
from database.database import YoutubeDataBase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
DATABASE_PATH = 'relational_database.db'

class SimpleTranscriber:
    def __init__(self):
        self.driver = None


    def _add_transcript(self, url, channel, db=None):
        """add a transcript to the Videos table in database
        Args:
            url: the link to the video
            channel: the channel associated with the video
            db: reference to database connection used to support class methods
        """
        if not self.driver:
            self.driver = webdriver.Chrome()
        
        self.driver.get(url)

        button_description = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "expand"))
        )
        button_description.click()

        button_transcript = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ytd-structured-description-content-renderer[@id='structured-description']//ytd-video-description-transcript-section-renderer[@class='style-scope ytd-structured-description-content-renderer']//div[@class='yt-spec-touch-feedback-shape__fill']"))
        )

        button_transcript.click()

        transcript_lines = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class='segment style-scope ytd-transcript-segment-renderer']"))
        )
        
        transcript_lines = [x.get_dom_attribute("aria-label") for x in transcript_lines]
        transcript = "\n".join(transcript_lines)

        if db:
            id = db.get_channel(channel)

            db.add_video(id, transcript, f"{channel}-Title", self.driver.current_url)
        else:
            with YoutubeDataBase(DATABASE_PATH) as db:
                id = db.get_channel(channel)

                db.add_video(id, transcript, f"{channel}-Title", self.driver.current_url)

    def find_phrase(self, phrase, channel):
        """
        Args:
            phrase: a str representing what to search in a transcript
            channel: a str representing the name/handle of a channel
        Returns:
            Returns: a list of tuple(video title, url) pertinent to the phrase otherwise returns
            None
        """
        matches = None
        with YoutubeDataBase(DATABASE_PATH) as db:
            # See if channel exists in database
            id = db.get_channel(channel)

            # Find videos of specified channel containing the phrase
            matches = db.find(id, '%' + phrase + '%')
        return matches

    def add_mock_channels(self):
        """Populate database to test functionality"""
        self.driver = webdriver.Chrome()
        with YoutubeDataBase(DATABASE_PATH) as db:
            # Add a some channels 
            db.add_channel("@git-amend", "git-amend")
            self._add_transcript("https://www.youtube.com/watch?v=X4Mbk54XqNk", "git-amend", db)
            db.add_channel("@codingunderpressure7818", "Coding Under Pressure")
            self._add_transcript("https://www.youtube.com/watch?v=eD2oAsalw7E", "coding under pressure", db)
        self.driver.close()
        
        
