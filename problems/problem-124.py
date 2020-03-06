import lib.utilities as ut
import time


if __name__ == "__main__":
    start = time.time()

    limit = 100000
    p = ut.primes_to(limit)
    R = []
    for i in range(1, limit + 1):
        nr = (i, ut.rad(i, p))
        R.append(nr)
    R.sort(key=lambda y: (y[1], y[0]))
    print(R[10000 - 1])
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
