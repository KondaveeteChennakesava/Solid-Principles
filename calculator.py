from data_extractor import DataExtractor
from data_analyzer import DataAnalyzer


class Calculator:
    def __init__(self, file_path, col1, col2,
                 label):
        self.col1 = col1
        self.col2 = col2
        self.label = label
        self.extractor = DataExtractor(file_path)

    def execute(self):
        data = self.extractor.extract_data()
        analyzer = DataAnalyzer(data, self.col1,
                                self.col2, self.label)
        return analyzer.get_min_diff_label()
