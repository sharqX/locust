import csv
import random

class ReadCsv():

    def __init__(self, file):
        try:
            file = open(file)
        except FileNotFoundError:
            print("File not Found")
    
        self.file = file
        self.reader = csv.DictReader(file)

    def read(self):
        return random.choice(list(self.reader))