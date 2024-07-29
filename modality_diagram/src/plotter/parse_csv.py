import csv
import os


class CsvFile:
    '''
        The input CSV file must be comma delimited and aligned on three columns.
        Each column represents one modality. Empty cells are counted as 0.
        Each row containing at least one value will be represented as a point.
    '''

    def __init__(self, file: str) -> None:
        self.file = file

    def parse_csv_file(self) -> list:

        # Get dir where script is located
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, self.file)

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data, binarization = [], []
            for row in reader:
                data.append(
                    tuple(float(cell) if cell else 0 for cell in row[:3]))
                binarization.append(
                    tuple(True if cell else False for cell in row[3:6]))

        return data, binarization
