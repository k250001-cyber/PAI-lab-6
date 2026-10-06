import numpy as np


def main():
    arr = np.array([12.0, np.nan, 25.0, 18.0, np.nan, 30.0, 22.0])

    print("NaN positions:", np.isnan(arr))
    print("NaN-aware mean:", np.nanmean(arr))
    print("NaN-aware sum:", np.nansum(arr))

    filled = np.where(np.isnan(arr), np.nanmean(arr), arr)

    print("Filled array:", filled)
    print("Any NaN remaining:", np.isnan(filled).any())


main()
