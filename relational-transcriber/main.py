"""A simple program that updates and queries a local database containing Youtube video information"""
from simple_transcriber.simple_transcriber import SimpleTranscriber
import sys 
def main():

    simple_transcriber = SimpleTranscriber()

    # Adding any argument will populate the database
    if len(sys.argv) > 1:
        # populate database
        simple_transcriber.add_mock_channels()

    # Ask user for query
    channel = input("Enter name/handle of channel: ")
    phrase = input("Enter phrase to find: ")
    matches = simple_transcriber.find_phrase(phrase, channel)

    if matches:
        print(matches)
    else:
        print(f"Could not find phrase \'{phrase}\' within channel \'{channel}\'")





if __name__ == "__main__":
    main()