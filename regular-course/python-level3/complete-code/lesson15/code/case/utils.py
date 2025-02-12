import csv


class CSVHandler:
    @staticmethod
    def save(fname, data):
        with open(fname, 'w', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    @staticmethod
    def load(fname):
        with open(fname, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            return list(reader)
