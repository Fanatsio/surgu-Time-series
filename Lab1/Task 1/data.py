import pandas as pd


class Data:
    def __init__(self, file_path):
        self.file = pd.read_csv(file_path)
        self.DAX_values = self.file['DAX']
        self.SMI_values = self.file['SMI']
        self.CAC_values = self.file['CAC']
        self.FTSE_values = self.file['FTSE']
