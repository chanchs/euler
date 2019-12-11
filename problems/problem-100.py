# Apparently Diophantine Pairs
import math
import time
import lib.utilities as ut


if __name__ == "__main__":
    start = time.time()

    limit = 1000000000000

    p = 1
    q = 2

    blue = red = 0

    if p == 1 and q == 2:
        blue = 15
        red = 6

        while blue + red < limit:
            red = 2 * blue + red - 1
            blue = blue + 2 * red

    print("blue = {}, red = {}, blue + red = {}".format(blue, red, blue + red))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
