import lib.utilities as ut
import time
import math


def number_of_divs(n, p):
    d = 0
    i = 0
    div = False
    if n in p:
        return 2
    while p[i] <= n:
        if n % p[i] == 0:
            d += 1
            n = int(n / p[i])
            div = True
        else:
            i += 1
            if div:
                d += 1
                div = False
    #if div:
    #    return d + 1
    #else:
    return d


def num_divisors(n):
    if n % 2 == 0:
        n /= 2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors *= (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors *= (count + 1)
        p += 2
    return divisors

if __name__=="__main__":
    start = time.time()
    pd, p = ut.sieve_of_eratosthenes(100)
    max_divs = 500

    n = 1
    while True:
        tr = int(n * (n + 1)/2)
        # if tr not in p:
        #     if n % 2 == 0:
        #         dn = num_divisors(n/2)
        #         dn_1 = num_divisors(n + 1)
        #         #print("n/2 = {0}, dn = {1}, (n + 1) = {2}, dn_1 = {3}".format(n/2, dn, n + 1, dn_1))
        #     else:
        #         dn = num_divisors(n)
        #         dn_1 = num_divisors((n + 1)/2)
        #         #print("n = {0}, dn = {1}, (n + 1)/2 = {2}, dn_1 = {3}".format(n, dn, (n + 1)/2, dn_1))
        # else:
        #     dn = 1
        #     dn_1 = 1
        dn = num_divisors(n)
        dn_1 = num_divisors(n + 1)

        print("{0} : {1}, d = {2}".format(n, tr, dn * dn_1))
        if dn * dn_1 >= max_divs:
            break
        n += 1

    end = time.time()

    print("Completed in {0:.2}s".format(end - start))
