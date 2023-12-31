import numpy as np

class Statistics:
    def get_values(self):
        values = []
        num_values = int(input("How many values do you want to add for calculation? "))
        for i in range(num_values):
            value = float(input(f"Enter value {i + 1}: "))
            values.append(value)
        return values

    def calculate_mean(self, data):
        return sum(data) / len(data)

    def calculate_standard_deviation(self, data):
        return np.std(data)

    def calculate_median(self, data):
        return np.median(data)

    def calculate_variance(self, data):
        return np.var(data)
