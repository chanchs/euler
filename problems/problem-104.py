# By definition,
# F(n) = F(n-1) + F(n-2)

import math
import time
import lib.utilities as ut


if __name__ == "__main__":
    start = time.time()
    k = 2749
    a = ut.n_th_fibonacci(k)
    k += 1
    b = ut.n_th_fibonacci(k)
    while True:
        first_nine = b // (10 ** int(math.log10(b) - 9 + 1))
        last_nine = b % 1000000000
        if ut.is_pandigital(last_nine):
            print(k)
            if ut.is_pandigital(first_nine):
                break
        temp = b
        b = a + b
        a = temp
        k += 1
    print(b)
    print(k)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
