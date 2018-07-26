import math
import time
import lib.utilities as ut

if __name__=="__main__":
    start1 = time.time()
    # That many primes under a million
    # https: // primes.utm.edu / howmany.html
    # takes about 3s to calculate
    p = ut.n_primes(78498)
    #p = ut.n_primes(100)
    print(p)
    start2 = time.time()
    circular_prime_count = 4
    for n in p:
        rotated = n
        print("prime : {}".format(n))
        little_count = 0
        exit_number = int(math.log(n, 10))
        for i in range(exit_number):
            rotated = ut.rotate(rotated, exit_number)
            if ut.is_prime(rotated):
                little_count += 1
            #print("Rotated {0} :: {1}, little_count :: {2}".format(i+1, rotated, little_count))
            if little_count == exit_number:
                circular_prime_count += 1
    print("Circular prime count = {}".format(circular_prime_count))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start2))
    print("Completed in {0:.2}s".format(end - start1))