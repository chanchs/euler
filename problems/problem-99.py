import math
import time
import lib.utilities as ut


if __name__ == "__main__":
    start = time.time()

    lst = []
    with open("problem-99.txt") as f:
        for line in f:
            b, e = line.split(",")
            lst.append(int(e) * math.log10(int(b)))

    big_line = 0
    for i in range(len(lst)):
        if lst[i] > lst[big_line]:
            big_line = i
    print("Largest = {}".format(big_line + 1))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
