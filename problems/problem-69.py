import math
import time
from lib.utilities import phi, primes_to

if __name__ == "__main__":
    print("Starting....")
    start = time.time()
    n = 1000000
    p = primes_to(int(math.sqrt(n)))
    ratio = big_ratio = 0
    big_n = 0
    for i in range(1, n + 1):
        print(i)
        _phi = phi(i, p)
        print(_phi)
        ratio = i / _phi
        print("n = {}, phi = {}, n/p = {}".format(i, _phi, ratio))

        if ratio > big_ratio:
            big_ratio = ratio
            big_n = i
    print("big ratio = {}, big n = {}".format(big_ratio, big_n))

    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))
