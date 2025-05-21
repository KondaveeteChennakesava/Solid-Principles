import csv


class DataExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_data(self):
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
