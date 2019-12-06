import lib.utilities as ut
import math
import time


if __name__ == "__main__":
    start = time.time()

    n = 50000000
    prime_sums = []

    p = ut.primes_to(math.sqrt(n))
    s = 0
    l = len(p)
    n2 = 0
    powers = []
    for i in range(l):
        t = [0, 0, 0]
        t[0] = p[i] * p[i]
        t[1] = p[i] * p[i] * p[i]
        t[2] = p[i] * p[i] * p[i] * p[i]
        powers.append(t)
    while n2 < l:
        n3 = 0
        while n3 < l and powers[n2][0] + powers[n3][1] < n:
            n4 = 0
            while n4 < 25 and powers[n2][0] + powers[n3][1] + powers[n4][2] < n:
                s = powers[n2][0] + powers[n3][1] + powers[n4][2]
                if s < n:
                    # if s not in prime_sums: (this takes forever, remove duplicates after)
                    prime_sums.append(s)
                    #print("{}^2 + {}^3 + {}^4 = {}".format(p[n2], p[n3], p[n4], s))
                n4 += 1
            n3 += 1
        n2 += 1
    # remove duplicates and count
    print("Count = {}".format(len(list(set(prime_sums)))))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

