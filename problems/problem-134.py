import lib.utilities as ut
import math
import time


if __name__ == "__main__2":
    start = time.time()

    # p = ut.primes_to(1000000)
    limit = 1000000
    p = ut.primes_to(limit + 10)
    print(limit)
    print(len(p), p)
    S = 0
    i = 2
    while p[i] <= limit:
        p1 = p[i]
        p2 = p[i + 1]

        shift = ut.tens(p1)
        product = shift + p1

        while product % p2 != 0:
            product += shift

        print(f"p1 = {p1}, p2 = {p2}, n = {product}, i = {i}")
        S += product
        i += 1

    print("S = {}".format(S))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))


def extended_gcd(a, b):
    s =0
    old_s = 1
    r = b
    old_r = a
    bezout_t = 0

    while r != 0:
        quotient = old_r // r
        old_r = r
        r = old_r - quotient * r
        old_s = s
        s = old_s - quotient * s

    if b != 0:
        bezout_t = (old_r - old_s * a) // b
    else:
        bezout_t = 0

    return [[old_s, bezout_t], old_r]


def chinese_remainder_theorem(p1, p2):
    m1 = p2
    m2 = ut.tens(p1)
    egcd = extended_gcd(m1, m2)
    r = p1 * egcd[0][0] * m1
    p = m1 * m2
    r %= p

    if r < 0 :
        r += p
    return r


if __name__ == "__main__":
    start = time.time()

    # limit = 100
    limit = 1000000
    p = ut.primes_to(limit+10)
    S = 0
    i = 2

    while p[i] <= limit:
        S += chinese_remainder_theorem(p[i], p[i + 1])
        i += 1

    print(S)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

