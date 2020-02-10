# Pulling out hair, another counting problem. Still hate them.

import lib.utilities as ut
import time


def F(m, n):
    s = [1] * m + [0] * (n - m + 1)
    for j in range(m, n + 1):
        s[j] = s[j] + s[j - 1] + s[j - m]
    return s[n] - 1


if __name__ == "__main__":
    start = time.time()

    n = 50
    print(F(2, n))
    print(F(3, n))
    print((F(4, n)))
    print(F(2, n) + F(3, n) + F(4, n))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
