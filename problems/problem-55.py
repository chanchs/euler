import math
import time
import lib.utilities as ut


def reverse(n):
    l = int(math.log10(n)) + 1
    m = 0
    for i in range(l):
        d = n % 10
        n = int(n / 10)
        m = m * 10 + d
    return m


if __name__ == "__main__":
    print("Starting....")
    start = time.time()
    limit = 10001
    loop_limit = 60
    count = 0
    for n in range(1, limit):
        m = 0
        #print(m)
        for i in range(loop_limit):
            m = n + reverse(n)
            #print(m)
            if ut.is_palindrome(m):
                count += 1
                #print(m)
                break
            else:
                n = m
        #print(m)
    print(limit - count - 1)

    end = time.time()
    print("Ending......")
    print("Completed in {0:.2}s".format(end - start))