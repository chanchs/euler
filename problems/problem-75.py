import lib.utilities as ut
import math
import time


if __name__ == "__main__":
    start = time.time()

    mx = 1500000
    u = v = 0
    u = 2
    E = True
    perimeter = [0] * mx
    s = 0
    while E:
        v += 1
        if (u + v) % 2 == 1 and ut.gcd(u, v) == 1:
            a = u * u + v * v
            b = u * u - v * v
            c = 2 * u * v
            p = a + b + c
            d = p
            if p <= mx:
                while d < mx:
                    perimeter[d] += 1
                    if perimeter[d] == 1:
                        s += 1
                    if perimeter[d] == 2:
                        s -= 1
                    d += p
        if v == u - 1:
            v = 0
            u += 1
        if u > math.sqrt(mx / 2):
            E = False
    print(s)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
