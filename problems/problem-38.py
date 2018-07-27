import math
import time
import lib.utilities as ut


if __name__=="__main__":
    start = time.time()

    start_number  = 1
    end_number = 9999
    large = 0
    for i in range(start_number, end_number):
        f = i * 1
        g = i * 2
        lf = int(math.log10(f) + 1)
        lg = int(math.log10(g) + 1)
        n = int(f * math.pow(10, lg) + g)
        if ut.is_pandigital(n) and n > large:
            large = n
    print(large)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
