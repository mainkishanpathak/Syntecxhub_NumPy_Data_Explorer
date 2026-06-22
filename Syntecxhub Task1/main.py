import numpy as np
from operationclass import IntArray


file_path = "company.txt"


def productivity(order, data):
    return np.sum(data[order])


def max_productivity(data):
    best = 0
    total = 0

    for i in range(len(data)):
        result = productivity(i, data)

        if result > total:
            total = result
            best = i + 1

    print(f"\nBest company: {best}")
    print(f"Products made: {total}")


def min_productivity(data):
    worst = 1
    total = productivity(0, data)

    for i in range(len(data)):
        result = productivity(i, data)

        if result < total:
            total = result
            worst = i + 1

    print(f"\nWorst company: {worst}")
    print(f"Products made: {total}")


def mean_products(data):
    print("\nAverage Products:")

    for i in range(len(data)):
        avg = np.mean(data[i])

        print(f"Company {i+1}: {avg:.2f}")


def load_file():
    rows = []

    with open(file_path, "r") as f:
        for line in f:
            rows.append(
                [int(x) for x in line.strip().split(",")]
            )

    return np.array(rows, dtype=object)


def main():

    data = load_file()

    first = IntArray(np.array(data[0]))

    # Terminal output first
    first.display()

    first.salary()

    max_productivity(data)

    min_productivity(data)

    mean_products(data)

    # Graph opens last
    first.show_data()


if __name__ == "__main__":
    main()