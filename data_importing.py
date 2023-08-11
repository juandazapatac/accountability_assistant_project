#Data importing

import csv

def import_data():
    with open('./accounting.csv') as csvfile:
        reader=csv.reader(csvfile)
        header=next(reader)
        return list(reader)