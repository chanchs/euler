import lib.utilities as ut
import time

if __name__=="__main__":
    start = time.time()
    n = 10001
    p = ut.n_primes(n)

    print("{0}th prime is {1}".format(n, p[-1]))

    end = time.time()

    print("Completed in {0:.2}s".format(end-start))