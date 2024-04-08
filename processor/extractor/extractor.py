import pandas as pd


class Extractor:
    """Extracts csv into pandas DataFrame."""

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def extract(self):
        return pd.read_csv(self.csv_file, delimiter=';')
