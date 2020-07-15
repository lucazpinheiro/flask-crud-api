import os
# from config import db
# from models import Person
from app import db, Character

# Data to initialize database with
INITIAL_DATA = [
    {'fname': 'Homer', 'lname': 'Simpson'},
    {'fname': 'Philip', 'lname': 'Fry'},
    {'fname': 'Bojack', 'lname': 'Horseman'}
]

# Delete database file if it exists currently
if os.path.exists('lite.db'):
    print('remove lite.db file')
    os.remove('lite.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for character in INITIAL_DATA:
    c = Character(lname = character['lname'], fname = character['fname'])
    db.session.add(c)

db.session.commit()
