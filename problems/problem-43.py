import math
import time
import lib.utilities as ut


if __name__=="__main__":
    start = time.time()

    n = 1406357289
    count = 0

    for n in range(1023456789, 9876543211):
        if ut.is_09_pandigital(n):
            d1 = int((n / 1000000000) % 10)
            d2 = int((n / 100000000) % 10)
            d3 = int((n / 10000000) % 10)
            d4 = int((n / 1000000) % 10)
            d5 = int((n / 100000) % 10)
            d6 = int((n / 10000) % 10)
            d7 = int((n / 1000) % 10)
            d8 = int((n / 100) % 10)
            d9 = int((n / 10) % 10)
            d10 = int((n) % 10)
            n1 = 100 * d2 + 10 * d3 + d4
            n2 = 100 * d3 + 10 * d4 + d5
            n3 = 100 * d4 + 10 * d5 + d6
            n4 = 100 * d5 + 10 * d6 + d7
            n5 = 100 * d6 + 10 * d7 + d8
            n6 = 100 * d7 + 10 * d8 + d9
            n7 = 100 * d8 + 10 * d9 + d10
            if n1 % 2 == 0 and n2 % 3 == 0 and n3 % 5 == 0 and n4 % 7 == 0 and n5 % 11 == 0 and n6 % 13 == 0 and n7 % 17 == 0:
                print(n)
                count += n

    print(count)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))