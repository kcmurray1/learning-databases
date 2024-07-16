# About
This is a project made to learn the basics about SQL using SQlite. Additionally, this aims to serve
as a template database class for future small scale projects.

# Usage
Install requirements
```bash
pip install -r requirements.txt
```
The system is executed on the command line
## Populate database with test data
Adding any additional arguments when running the system will populate any connected database.
```bash
python main.py test
```
Otherwise simply running
```bash
python main.py
```
will skip the population step and prompt the user to enter a channel and phrase to search for.  
The command line will display any videos from the specified channel that contain the entered phrase.
