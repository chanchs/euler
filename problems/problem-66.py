import time
import math

if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    bigX = bigD = 0
    for D in range(1001):
        m = 0
        d = 1
        h1 = 1
        h2 = 0
        k1 = 0
        k2 = 1
        hn = kn = 0
        Ds = 0
        print()
        print("D = {} : ".format(D), end=" ")
        a0 = a = math.floor(math.sqrt(D))
        key = False
        if a0 * a0 != D:
            while Ds != 1:
                m = d * a - m
                d = (D - m * m) / d
                hn = a * h1 + h2
                kn = a * k1 + k2
                Ds = hn * hn - D * kn * kn
                print("hn = {}, kn = {}, Ds = {}".format(hn, kn, Ds))
                h2 = h1
                k2 = k1
                h1 = hn
                k1 = kn
                a = math.floor((a0 + m) / d)
        if hn > bigX:
            bigX = hn
            bigD = D
    print("Largest x = {}, for D = {}".format(bigX, bigD))
    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))