# https://rosettacode.org/wiki/Knuth%27s_power_tree
# https://en.wikipedia.org/wiki/Addition-chain_exponentiation
# 

import lib.utilities as ut
import math
import time


limit = 200
cost = [1000000000000000] * (limit + 1)
path = [0] * (limit + 1)


def backtrack(power, depth):
    if power > limit or depth > cost[power]:
        return
    cost[power] = depth
    path[depth] = power
    for i in range(depth, -1, -1):
        backtrack(power + path[i], depth + 1)


if __name__ == "__main__":
    start = time.time()

    result = 0
    backtrack(1, 0)

    for i in range(1, limit + 1):
        result += cost[i]
    print(result)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
