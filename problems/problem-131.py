import lib.utilities as ut
import time

"""
n^3 + n^2p = x^3
n^3(1 + p/n) = x^3
n^3( (n + p) / n ) = x^3
n cube_root( (n + p)/n ) = x
n cube_root(p + n) / cube_root(n) = x

For x to be integer, both p + n and n must be perfect cubes.

n = a^3 and  (p + n) = b^3

then,

p + n = b^3
p + a^3 = b^3
p = b^3 - a^3
p = (b - a) (b^2 + b * a + a^2) 
"""


if __name__ == "__main__":
    start = time.time()

    limit = 1000000
    count = 0
    # primes = ut.primes_to(limit)

    #print(primes)
    print(limit, count)

    r = 0
    x = 0
    while True:
        r = (x + 1) * (x + 1) * (x + 1) - x * x * x
        if r >= limit:
            break
        if ut.is_prime1(r):
            print(r)
            count += 1
        x += 1

    print(count)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
