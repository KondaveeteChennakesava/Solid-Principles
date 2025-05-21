class DataAnalyzer:
    def __init__(self, data, col1, col2, label):
        self.data = data
        self.col1 = col1
        self.col2 = col2
        self.label = label

    def get_min_diff_label(self):
        min_diff = float('inf')
        result_label = None
        for row in self.data:
            val1 = int(row[self.col1])
            val2 = int(row[self.col2])
            diff = abs(val1 - val2)

            if diff < min_diff:
                min_diff = diff
                result_label = row[self.label]

        return result_label
