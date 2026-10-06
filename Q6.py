import numpy as np


def simulate(seed):
    rng = np.random.default_rng(seed)
    data = rng.normal(loc=50, scale=10, size=1000)
    mean = np.mean(data)
    std = np.std(data)

    print("Seed:", seed)
    print("Mean:", mean)
    print("Median:", np.median(data))
    print("Standard deviation:", std)
    print("Minimum:", np.min(data))
    print("Maximum:", np.max(data))
    print("Percentage within one standard deviation:", np.sum(np.abs(data - mean) <= std) / data.size * 100)


def main():
    simulate(42)
    simulate(7)
    print("Comparison: the two seeds give similar but not identical statistics because each seed generates a different sample.")


main()
