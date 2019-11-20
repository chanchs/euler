import lib.utilities as ut
import time


if __name__ == "__main__":
    start = time.time()

    limit = 100
    s = range(1, limit + 1)
    print(len(s))
    c = ut.count(s, limit, limit - 2)
    print(c)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
