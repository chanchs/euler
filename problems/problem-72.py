from lib.utilities import phi1, primes_to, phi2
import math
import time


if __name__ == "__main__1":
    print("Starting....")
    start = time.time()

    fraction_count = 0
    N = 1000000
    p = primes_to(N + 1)
    print("Done calculating the primes")
    for n in range(2, N + 1):
        fraction_count = fraction_count + phi1(n, p)
    print(fraction_count)
    end = time.time()

    print("Ending......")
    print("Completed in {:.2}s".format(end - start))

if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    N = 1000000
    # need to subtract one to discount phi(1) = 1
    print(sum(phi2(N)) - 1)
    end = time.time()

    print("Ending......")
    print("Completed in {:.2}s".format(end - start))
