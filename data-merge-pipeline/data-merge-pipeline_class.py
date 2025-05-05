import json
import csv

class DataHandler:
    """
    A class to handle basic data operations such as reading, renaming, merging, and saving CSV/JSON data.
    """

    def __init__(self, path, file_type):
        self.file_type = file_type
        self.path = path
        self.data = self.load_data()
        self.columns = self.get_columns()
        self.num_rows = self.get_size()

    def load_json(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def load_csv(self):
        data_csv = []
        with open(self.path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_csv.append(row)
        return data_csv

    def load_data(self):
        if self.file_type == 'csv':
            return self.load_csv()
        elif self.file_type == 'json':
            return self.load_json()
        else:
            raise ValueError("Unsupported file type. Use 'csv' or 'json'.")

    def get_columns(self):
        return list(self.data[0].keys()) if self.data else []

    def rename_columns(self, mapping):
        """
        Rename columns based on a provided dictionary mapping.
        """
        new_data = []
        for row in self.data:
            new_row = {mapping.get(k, k): v for k, v in row.items()}
            new_data.append(new_row)
        self.data = new_data
        self.columns = self.get_columns()

    def get_size(self):
        return len(self.data)

    @staticmethod
    def join(dataA, dataB):
        """
        Merge data from two DataHandler instances into a new one.
        """
        if not isinstance(dataA, DataHandler) or not isinstance(dataB, DataHandler):
            raise TypeError("Both inputs must be instances of DataHandler.")

        merged = DataHandler.__new__(DataHandler)
        merged.file_type = 'csv'
        merged.path = None
        merged.data = dataA.data + dataB.data
        merged.columns = dataA.columns
        merged.num_rows = len(merged.data)
        return merged

    def to_table_format(self):
        """
        Converts internal data to list-of-lists format, including header.
        """
        table = [self.columns]
        for row in self.data:
            line = [row.get(col, 'Unavailable') for col in self.columns]
            table.append(line)
        return table

    def save_to_csv(self, output_path):
        """
        Save the processed data to a CSV file.
        """
        table = self.to_table_format()
        with open(output_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(table)
