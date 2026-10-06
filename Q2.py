import numpy as np


def main():
    features = np.array([
        [5.1, 3.5, 1.4, 0.2],
        [4.9, 3.0, 1.4, 0.2],
        [6.2, 3.4, 5.4, 2.3],
        [5.9, 3.0, 5.1, 1.8],
        [5.5, 2.3, 4.0, 1.3],
        [6.5, 2.8, 4.6, 1.5],
        [5.7, 2.8, 4.5, 1.3],
        [6.3, 3.3, 6.0, 2.5],
        [4.7, 3.2, 1.3, 0.2],
        [7.1, 3.0, 5.9, 2.1]
    ])

    mean = np.mean(features, axis=0)
    std = np.std(features, axis=0)
    standardized = (features - mean) / std

    print("Mean:", mean)
    print("Standard deviation:", std)
    print("Standardized features:")
    print(standardized)
    print("Standardized means:", np.mean(standardized, axis=0))
    print("Standardized standard deviations:", np.std(standardized, axis=0))
    print("Broadcasting: mean and std have shape (4,) and features has shape (10, 4), so NumPy applies the subtraction and division to every row without loops.")


main()
