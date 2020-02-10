# Another fucking counting problem. Still hate them.

import lib.utilities as ut
import time


if __name__ == "__main__":
    start = time.time()

    n = 50
    s = [1]

    while s[-1] < 1000000:
        s += [sum(s[:-n]) + s[-1]]

    print(s)
    print(len(s))
    print(len(s) - 2)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
