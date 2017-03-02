import lib.utilities as ut
import math
import time

if __name__=="__main__":
    print("problem 3")
    x = 600851475143
    start = time.time()
    sqrt_x = int(math.sqrt(x))
    pb, p = ut.sieve_of_eratosthenes(sqrt_x)

    large = p[0]

    for i in p:
        if x % i == 0:
            print(i)
            large = i
    print(large)
    stop = time.time()

    print("Completed in {0:.2f}s".format(stop-start))