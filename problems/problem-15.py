import lib.utilities as ut
import time


if __name__ == "__main__":
    start = time.time()
    limit = 20

    p = ut.binomial(2 * limit, limit)

    print(p)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
