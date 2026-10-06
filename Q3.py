import numpy as np


def main():
    image = np.array([
        [12, 45, 200, 255, 180, 30],
        [60, 130, 220, 240, 90, 15],
        [75, 150, 128, 210, 100, 40],
        [20, 110, 190, 170, 140, 5],
        [0, 85, 160, 230, 120, 55],
        [35, 95, 205, 250, 70, 25]
    ])
    threshold = 128

    mask = image > threshold
    thresholded = np.where(mask, 255, 0)

    print("Minimum intensity:", np.min(image))
    print("Maximum intensity:", np.max(image))
    print("Mean intensity:", np.mean(image))
    print("Binary mask:")
    print(mask)
    print("Thresholded image:")
    print(thresholded)


main()
