# I still hate counting problems

"""
The relationship with A005252 comes from the second definition there: "number of n-bit sequences that
avoid both 010 and 0110", which is pretty much what we are looking for with 1=red, 0=black.
Add an extra black at each end to make them identical.

"""

import lib.utilities as ut
import time


if __name__ == "__main__":
    start = time.time()

    n = 50 + 1
    s = 0

    for k in range(n // 4 + 1):
        s += ut.nCr(n - 2 * k, 2 * k)

    print(s)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
