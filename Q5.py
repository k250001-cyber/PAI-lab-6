import numpy as np


def main():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("A shape:", A.shape, "B shape:", B.shape)
    print("A + B:")
    print(A + B)

    print("A shape:", A.shape, "B shape:", B.shape)
    print("A - B:")
    print(A - B)

    print("A shape:", A.shape, "B shape:", B.shape)
    print("A * B:")
    print(A * B)

    print("A shape:", A.shape, "B shape:", B.shape)
    print("A @ B:")
    print(A @ B)

    print("A shape:", A.shape)
    print("Transpose of A:")
    print(A.T)

    print("A shape:", A.shape)
    print("Determinant of A:", np.linalg.det(A))

    print("A shape:", A.shape)
    print("Inverse of A:")
    print(np.linalg.inv(A))

    print("Addition, subtraction and element-wise multiplication require the same (or broadcastable) shapes.")
    print("Matrix multiplication requires the columns of A to equal the rows of B.")
    print("Determinant and inverse require a square matrix.")


main()
