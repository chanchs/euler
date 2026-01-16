# https://blog.dreamshire.com/project-euler-140-solution/

from setuptools.dist import sequence
import lib.utilities as ut
import math
import time

# https://oeis.org/A081018
# Nth golden nugget = 2Nth Fibonacci x (2N+1) Fibonacci

def G(n):
    a, b = 1, 4
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        sequence = [1, 4]
        for _ in range(2, n):
            next_g = a + b
            sequence.append(next_g)
            a, b = b, next_g
    return sequence

if __name__ == "__main__":
    start = time.time()
    #gn_20 = G(100)
    #print(211345365)
    #print(gn_20)
    #print(gn_20[2 * 19] + gn_20[2 * 19 + 1])
    #print(gn_20[20] * gn_20[20 + 1])
    #print(sum(gn_20[:20]))
    #sum = gn_20[2 * 19] * gn_20[2 * 19 + 1]
    #print(f"Sum = {sum}")
    limit = 30
    sqrt_5 = 5 ** 0.5
    f = [7, 14, 50, 97]

    for i in range(limit - 4):
        f.append(7 * f[-2] - f[-4])
    print(f)
    s = 0
    for x in f:
        s += int(x / sqrt_5) - 1
    print(s)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

