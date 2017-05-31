import math
import time
import lib.utilities as ut


if __name__=="__main__":
    start = time.time()
    ss = 0
    for x in range(10, 99999):
        digits = ut.get_digits(x)
        s = 0
        for digit in digits:
            s += math.factorial(digit)
        if s == x:
            print("{} is curious".format(x))
            ss += s
    print(ss)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))