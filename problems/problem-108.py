# https://www.mathpages.com/home/kmath332.htm

import math
import time
import lib.utilities as ut


"""
        /*
         *
         * 1/x + 1/y = 1/n
         * => (x + y)/xy = 1/n
         * => n(x + y) = xy
         * => xy - n(x + y) = 0
         * => xy - n(x + y) + n*n = n*n
         * => xy - nx - ny + n*n = n*n
         * => x(y - n) - n(y - n) = n*n
         * => (y - n) (x - n) = n*n
         *
         * => number of solutions for y & x is the number of factors of n*n
         * => number of *distinct* solution pairs for x and y is (E + 1) / 2 where E is the number of factors of n*n
         * => we exclude 1 and E as a divisor of n*n
         */
"""


if __name__ == "__main__":
    start = time.time()

    n = 2 * 3 * 5 * 7 * 11

    while True:
        print(n)
        d = 2
        n_sq = n * n
        for i in range(2, n):
            if n_sq % i == 0:
                d += 1
        if d > 1000:
            break
        n += 2 * 3 * 5 * 7 * 11

    print("Answer = {}".format(n))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))



# slow
if __name__ == "__main__1":
    start = time.time()

    n = 1
    while True:
        n_sq = n * n
        f = ut.factor(n_sq)
        E = len(f[0]) - 2
        d = (E + 1) / 2
        #print(f, len(f[0]), E)
        print(n)
        if d > 1000:
            break
        else:
            n += 1

    print("Answer = {}".format(n))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
