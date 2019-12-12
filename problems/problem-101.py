# Lagrange method to solve polynomial roots
# https://en.wikipedia.org/wiki/Lagrange_polynomial
import math
import time
import lib.utilities as ut


if __name__ == "__main__":
    start = time.time()

    coefficients = [1, -1,  1, -1, 1, -1, 1, -1, 1, -1, 1]
    l = len(coefficients)
    p = ut.Polynomial(coefficients=coefficients)

    y = [0] * l

    for x in range(l):
        y[x] = p.evaluate(x + 1)
    print(y)

    fits = 0
    for n in range(len(coefficients)):
        result = 0
        for i in range(1, n + 1):
            temp1 = temp2 = 1
            for j in range(1, n + 1):
                if i != j:
                    temp1 = temp1 * (n + 1 - j)
                    temp2 = temp2 * (i - j)
            result = result + temp1 * y[i - 1] // temp2
        fits = fits + result
        print(result)
    print("FITs = {}".format(fits))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
