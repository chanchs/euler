import math
import time
import lib.utilities as ut


def is_truncable_prime(p):
    prm = p
    l = int(math.log(p, 10))
    prime_count = 0
    prm1 = p
    for i in range(0, l):
        prm = int(prm / 10)
        number1 = int(prm1 % int(math.pow(10, l - i)))
        if ut.is_prime(prm) and ut.is_prime(number1):
            prime_count += 1
    if prime_count == l:
        return True
    else:
        return False


if __name__=="__main__":
    start = time.time()
    truncable_prime_count = 0
    sum_of_truncable_primes = 0
    p = 11
    E = True
    while E:
        if ut.is_prime(p):
            if is_truncable_prime(p):
                print("{} is truncable prime".format(p))
                truncable_prime_count += 1
                sum_of_truncable_primes += p
            if truncable_prime_count == 11:
               E = False
        p += 2
    print("sum of {0} truncable primes = {1}".format(truncable_prime_count, sum_of_truncable_primes))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
