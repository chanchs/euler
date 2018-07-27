import math
import time
import lib.utilities as ut


if __name__=="__main__":
    start = time.time()
    N = 1000001
    x = 0
    y = 0
    d = 1
    for i in range(1, N):
        #print(i)
        l = int(math.log10(i)) + 1
        x = x * pow(10, l) + i
    print(x)
    print(y)
    d1 = ut.get_nth_digit(x, 1)
    d10 = ut.get_nth_digit(x, 10)
    d100 = ut.get_nth_digit(x, 100)
    d1000 = ut.get_nth_digit(x, 1000)
    d10000 = ut.get_nth_digit(x, 10000)
    d100000 = ut.get_nth_digit(x, 100000)
    d1000000 = ut.get_nth_digit(x, 1000000)

    print("d1 = {0}, d10 = {1}, d100 = {2}, d1000 = {3}, d10000 = {4}, d100000 = {5}, d1000000 = {6}".format(
        d1, d10, d100, d1000, d10000, d100000, d1000000))
    d = d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
    print("d = {}".format(d))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
