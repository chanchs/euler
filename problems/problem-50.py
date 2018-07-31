import math
import time
import lib.utilities as ut

if __name__ == "__main__":
    start = time.time()

    p = ut.n_primes(80000)

    print(p)

    limit = 1000000
    count = 0
    max_sum = 0
    max_run = -1

    for i in range(count, len(p)):
        sum =0
        for j in range(i, len(p)):
            sum += p[j]
            if sum > limit:
                break
            if ut.is_prime(sum) and sum > max_sum and j - i > max_run:
                max_run = j - i
                max_sum = sum
    print(max_sum)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
