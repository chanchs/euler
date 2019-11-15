from lib.utilities import n_phi, primes_to, is_permutation, phi, phi1
import math
import time


if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    n = 8319823
    primes = primes_to(int(math.sqrt(n)))

    n_p = n_phi(n)
    _phi = phi1(n)
    p = round(n / n_p)
    print(n, p, _phi, is_permutation(n, p), is_permutation(n, _phi), n / _phi)

    max = 10000000
    small_ratio = 1000
    small_n = 0
    ratio = 0
    small_p = 0

    primes = primes_to(10000)

    for n in range(8000000, max):
        p = phi1(n)
        if is_permutation(p, n):
            ratio = n / p
            if ratio < small_ratio and ratio != 1:
                small_ratio = ratio
                small_n = n
                small_p = p
                print("n = {}, phi = {}, ratio = {}".format(n, p, ratio))
    print("small n = {}, small phi = {}, small ratio = {}".format(small_n, small_p, small_ratio))

    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))
