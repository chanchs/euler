import lib.utilities as ut
import math
import time



if __name__ == "__main__":
    start = time.time()

    #limit = 100000
    limit = 1000000000000
    sol = set()

    for z in range(2, int(limit ** (1/3)) + 1):
        for y in range(1, z):
            if z * z * z * y + y * y > limit:
                break
            for x in range(1, int(limit / (y * z * z * z)) + 1):
                n = z * z * z * x * x * y + x * y * y
                if n > limit:
                    break
                else:
                    if ut.is_square(n):
                        sol.add(n)
    print(sum(sol))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

