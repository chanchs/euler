import math
import time
import lib.utilities as ut


if __name__=="__main__":
    start = time.time()
    solutions = {0: 0}
    N = 1000
    for x in range(1, N + 1):
        y = x + 1
        z = y + 1
        while z <= N:
            while z * z < x * x + y * y:
                z = z + 1
            if z * z == x * x + y * y and z <= N:
                p = x + y + z
                if p <= 1000:
                    if p in solutions:
                        solutions[p] = solutions[p] + 1
                    else:
                        solutions[p] = 1
            y = y + 1
    v = list(solutions.values())
    k = list(solutions.keys())
    print("Number of Exact solutions for p = {0}, solutions = {1}".format(k[v.index(max(v))], max(v)))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))