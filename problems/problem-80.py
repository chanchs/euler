# 40886
import lib.utilities as ut
# I hate this solution, make the commented code work out
from decimal import *
import time


if __name__ == "__main__":
    start = time.time()

    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    s = 0

    getcontext().prec = 102
    for n in range(101):
        if n not in squares:
        #    a = 5 * n
        #    b = 5
        #    while int(math.log10(b) + 1) < 101:
        #        if a >= b:
        #            a -= b
        #            b += 10
        #        else:
        #            a *= 100
        #            b = 10 * b - 45
            b = Decimal(n).sqrt()
            b_str = str(b).replace(".", "")
            b_str = b_str[0:100]
            for d in b_str:
                s += int(d)
            print("b = {} n = {}, s = {}".format(Decimal(b), n, s))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
