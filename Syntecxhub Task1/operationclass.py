import numpy as np
import matplotlib.pyplot as plt


class IntArray:
    def __init__(self, int_array):
        if not isinstance(int_array, np.ndarray):
            raise ValueError("Input must be NumPy array")

        self.int_array = int_array.astype(int)

    def display(self):
        print("\nEmployee Productivity:")
        print(self.int_array)

    def salary(self):
        salaries = self.int_array * 7
        print("\nSalary Calculation:")
        print(salaries)

    def show_data(self):
        x = np.arange(len(self.int_array))

        plt.plot(x, self.int_array, marker="o")

        plt.title("Employee Productivity")
        plt.xlabel("Employee")
        plt.ylabel("Products")

        plt.grid()
        plt.show()