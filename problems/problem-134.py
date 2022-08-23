import lib.utilities as ut
import math
import time


if __name__ == "__main__":
    start = time.time()

    p = ut.primes_to(100000)



    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
