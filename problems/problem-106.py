# I have no clue how or why this works. Cheated

import itertools
import functools
import math
import time
import lib.utilities as ut


def filt_func(c1, c2):
    if c1[0] > c2[0]:
        return False
    return not functools.reduce(lambda x, y: x and (y[0] < y[1]), itertools.zip_longest(sorted(c1), sorted(c2)), True)


def generator(n, k):
    s1 = itertools.combinations(range(n), k // 2)
    comb_total = []
    for comb1 in s1:
        left_nums = set(range(n)) - set(comb1)
        s2 = (c for c in itertools.combinations(left_nums, k // 2) if filt_func(comb1, c))
        comb_total.extend(itertools.product([comb1], s2))
    return comb_total


if __name__ == "__main__":
    start = time.time()

    result = sum(len(generator(12, i)) for i in range(4, 13, 2))
    print("The result is:", result)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
