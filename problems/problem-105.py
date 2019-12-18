import math
import time
import lib.utilities as ut


if __name__ == "__main__":
    start = time.time()
    with open("problem-105.txt") as f:
        for line in f:
            s = [int(x) for x in list(line.strip().split(","))]
            print(s)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
