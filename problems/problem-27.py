import time
import lib.utilities as ut
import math

if __name__=="__main__":
    start = time.time()

    n, a, b = 0, 0, 0
    big_a, big_b = 0, 0
    prime_count, big_prime_count = 0, 0
    f = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            f = math.fabs(n * n + a * n + b)
            prime_count = 0

            while ut.is_prime(f):
                prime_count += 1
                n += 1
                f =  math.fabs(n* n + a * n + b)

            if prime_count > big_prime_count:
                big_prime_count = prime_count
                big_a = a
                big_b = b
                print("current big a = {0} and b = {1}, prime count = {2}, n = {3}, a * b = {4}".format(a, b,
                                                                                prime_count, n, a * b))

    print("biggest a = {0}, b = {1}, a * b = {2} produces : {3} primes for n ={4}".format(big_a, big_b, big_a*big_b,
                                                                               big_prime_count, n))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))