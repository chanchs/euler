import math
import time
import lib.utilities as ut


if __name__ == "__main__":
    """
    This works because operator // floors the result after division
    """
    print("Starting....")
    start = time.time()

    big = 0
    for a in range(1, 100):
        for b in range(1, 100):
            n = a ** b
            l = int(math.log10(n)) + 1
            print(l)
            s = 0
            print(n)
            for i in range(l):
                d = n % 10
                s += d
                n = int(n // 10)
                #print(n, s, d)
            if s > big:
                big = s

    print(big)



    end = time.time()
    print("Ending......")
    print("Completed in {0:.2}s".format(end - start))