import numpy as np


def main():
    marks = np.array([
        [78, 85, 62, 90, 74],
        [45, 52, 38, 60, 41],
        [88, 92, 95, 84, 91],
        [35, 40, 28, 45, 33],
        [66, 70, 58, 72, 64],
        [50, 48, 55, 52, 47],
        [92, 87, 90, 95, 89],
        [30, 25, 42, 38, 35],
        [72, 68, 75, 80, 70],
        [55, 60, 49, 58, 62]
    ])

    totals = np.sum(marks, axis=1)
    averages = np.mean(marks, axis=1)
    subject_averages = np.mean(marks, axis=0)
    top_student = np.argmax(averages)
    passed = np.sum(averages >= 50)
    result = np.where(averages >= 50, "Pass", "Fail")

    print("Student totals:", totals)
    print("Student averages:", averages)
    print("Subject averages:", subject_averages)
    print("Highest average student index:", top_student)
    print("Students with average >= 50:", passed)
    print("Result:", result)


main()
