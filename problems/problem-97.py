import lib.utilities as ut
import math
import time


if __name__ == '__main__':
    start = time.time()

    p = 28433
    for j in range(1, 7830457 + 1):
        p *= 2
        p = p % 10000000000
    p += 1
    print(p)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))


if __name__ == '__main__1':
    start = time.time()

    p = 1
    pt = 1

    for i in range(7830457):
        pt = (pt * 2)
        #if math.log10(pt) > 10:
        #    pt = int(pt / 10000000000)
        #print("step {}, p = {}".format(i, pt))
        print(i)

    print("2^7830457 = {}".format(pt))
    p = 28433 * pt
    print("28433 * 2^7830457 = {}".format(p))
    p += 1
    p = p % 10000000000
    print("28433 * 2^7830457 + 1 = {}".format(p))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
