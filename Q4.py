import numpy as np


def main():
    readings = np.array([
        [22.5, 23.1, 24.0, 25.2, 26.8, 27.5],
        [30.2, 31.5, 29.8, 32.0, 33.1, 31.0],
        [18.4, 19.0, 20.2, 19.5, 21.0, 20.8],
        [25.0, 26.3, 27.1, 28.4, 29.0, 30.5],
        [21.7, 22.0, 23.5, 22.8, 24.1, 23.0]
    ])
    threshold = 28

    mean = np.mean(readings, axis=1)

    print("Per-sensor mean:", mean)
    print("Per-sensor minimum:", np.min(readings, axis=1))
    print("Per-sensor maximum:", np.max(readings, axis=1))
    print("Per-sensor standard deviation:", np.std(readings, axis=1))
    print("Sensor with highest average reading:", np.argmax(mean))
    print("Readings above threshold:")
    print(readings > threshold)


main()
