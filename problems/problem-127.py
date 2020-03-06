# This solutions works because, rad(a) * rad(b) * rad(c) = rad(a * b * c), and
# a + b = c
# if gcd(a, b) = 1 and gcd(b, c) = 1 then, gcd(a, c) = 1

import lib.utilities as ut
import time


if __name__ == "__main__":
    start = time.time()

    limit = 120000
    p = ut.primes_to(limit)
    R = []
    for i in range(1, limit + 1):
        nr = ut.rad(i, p)
        R.append(nr)
    print("Complete calculating radicals")

    result = 0
    for a in range(1, limit):
        for b in range(a + 1, limit - a):
            if R[a - 1] * R[b - 1] * R[a + b - 1] < a + b and ut.gcd(a, b) == 1:
                print(a + b)
                result += a + b
    print(result)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
