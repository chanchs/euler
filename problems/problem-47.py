import math
import time
import lib.utilities as ut


def distinct_prime_factors(n, sorted=False, distinct=True):
    limit = (int)(math.sqrt(n)) + 1
    p = ut.n_primes(limit)
    if ut.is_prime(n):
        return [n]
    ff = []
    if n % p[0] == 0:
        ff.append(p[0])
        n = int(n / p[0])
        if n in p:
            ff.append(n)
    for primes in p:
        if n % primes == 0 and primes not in ff:
            ff.append(primes)
            n = int(n / primes)
            if n in p and (n not in ff != distinct):
                ff.append(n)
    if sorted:
        ff.sort()
    return ff


if __name__ == "__main__":
    start = time.time()
    E = False
    num_factors = 4
    n = 0
    count = 0
    nums = []
    while E is not True:
        n += 1
        print(n)
        if len(distinct_prime_factors(n)) == num_factors:
            count += 1
            nums.append(n)
            if count == num_factors:
                E = True
                break
        else:
            count = 0
            nums = []
    print(nums)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))