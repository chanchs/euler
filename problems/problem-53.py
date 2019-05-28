import math
import time
import lib.utilities as ut


def nCr(n, r):
    if r > n:
        temp = r
        r = n
        n = temp
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    count = 0
    for n in range(101):
        for r in range (n):
            ncr = nCr(n, r)
            if ncr > 1000000:
                print("nCr({0}, {1}) = {2}".format(n, r, ncr))
                count += 1
    print("count = {}".format(count))

    end = time.time()
    print("Ending......")
    print("Completed in {0:.2}s".format(end - start))