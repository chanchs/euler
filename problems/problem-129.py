import lib.utilities as ut
import time


if __name__ == "__main__":
    print("Starting....")
    start = time.time()
    limit = 1000001
    n = limit
    while ut.A(n) < limit:
        n += 2
    print(n)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
