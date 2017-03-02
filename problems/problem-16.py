import lib.utilities as ut
import math
import time


if __name__=="__main__":
    start = time.time()
    # n = []
    # e = 1000
    # b = 2
    # n.append(1)
    #
    # for i in range(e):
    #     carry = 0
    #     for index in range(len(n)):
    #         number = n[index] * b + carry
    #         if number < 10:
    #             n[index] = number
    #             carry = 0
    #         else:
    #             n[index] = number % 10
    #             carry = int(number / 10)
    #
    #     if carry > 0:
    #         n.append(carry)
    n = ut.big_pow(2, 1000)
    print(n)
    s = 0
    for i in range(len(n)):
        s += n[i]

    print("sum = {}".format(s))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))