import math
import time
import lib.utilities as ut

if __name__ == "__main__":
    """
    (a * b) % c = ((a % c) * (b % c)) % c
    (a + b) % c = ((a % c) + (b % c)) % c
    """
    start = time.time()
    digits = 1000
    d = 10000000000
    s = 0
    for i in range(1, digits + 1):
        #print(i)
        t = i
        for y in range(1, i):
            t = t * i
            t = t % d
        s = s + t
        s = s % d
    print(s)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))