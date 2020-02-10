# I hate counting problems

import lib.utilities as ut
import time


if __name__ == "__main__":
    start = time.time()
    print(ut.nCr(6 + 10, 10) + ut.nCr(6 + 9, 9) - 2 - 6 * 10)
    print(ut.nCr(10 + 10, 10) + ut.nCr(10 + 9, 9) - 2 - 10 * 10)
    print(ut.nCr(100 + 10, 10) + ut.nCr(100 + 9, 9) - 2 - 100 * 10)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
