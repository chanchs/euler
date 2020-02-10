import math
import time
import lib.utilities as ut


if __name__ == "__main__":
    start = time.time()
    sum_of_s = 0
    with open("problem-105.txt") as f:
        for line in f:
            s = [int(x) for x in list(line.strip().split(","))]
            if ut.is_special_sum_set(s):
                print(s)
                sum_of_s += sum(s)
    print("Sum of optimum = {}".format(sum_of_s))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
