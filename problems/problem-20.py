import math
import time


if __name__=="__main__":
    start = time.time()
    n = 100
    N = math.factorial(n)
    print(N)
    d = int(math.log10(n) + 1)
    s = 0
    while N > 0:
        d0 = N % 10
        s += d0
#       print("N = {0}, s = {1}, d0 = {2}".format(N, s, d0))
        N = int(N // 10)
    print("sum = {}".format(s))
    end1 = time.time()
    print("Completed in {0:.2}s".format(end1 - start))
