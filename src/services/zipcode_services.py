from src.db import User, ZipCodesRatings, db
import csv
import os

def identify_zipcode(user):
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(parent_dir, "../constants/us_postal_codes.csv")
    filename = os.path.abspath(os.path.realpath(filepath))
    
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for line in reader:
            if line[0] == user.zipcode:
                user.city = line[1]
                user.state = line[2]
                db.session.commit()
