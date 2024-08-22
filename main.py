import matrix.plu as plu
import sys
import numpy as np


def read_matrix(filename):
    return np.loadtxt(filename, delimiter=",")


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    verbose = False

    if len(sys.argv) == 3:
        verbose = True

    filename = sys.argv[1]
    A = read_matrix(filename)

    print("Input solution vector 'b':")
    input_vector = input()
    b = np.array(input_vector.split(",")).astype(np.float64)

    P, L, U = plu.plu_decomposition(A)

    if verbose:
        print("P-Transposed:")
        print(P.T)
        print("L:")
        print(L)
        print("U:")
        print(U)

    x = plu.solve_plu(P, L, U, b)
    print("Solution:")
    print(x)


if __name__ == "__main__":
    main()
