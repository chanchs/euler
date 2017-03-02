import lib.utilities as ut
import time


if __name__=="__main__":
    start = time.time()
    limit = 2000000
    bp, p = ut.sieve_of_eratosthenes(limit)
    s = sum(p)
    #print(p)
    print("sum of primes below {0} is {1}".format(limit, s))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))