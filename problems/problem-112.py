import lib.utilities as ut
import math
import time


def is_bouncy(n):
    last = n % 10
    n = n // 10
    a = d = False
    while n > 0:
        nxt = n % 10
        n = n // 10
        if nxt < last:
            a = True
        elif nxt > last:
            d = True
        last = nxt
        if a and d:
            return True
    return a and d


if __name__ == "__main__":
    start = time.time()

    print(is_bouncy(155349))
    print(is_bouncy(11))
    print(is_bouncy(538))
    print(is_bouncy(4321))
    print(is_bouncy(1204))
    print(is_bouncy(134468))
    print(is_bouncy(66420))
    print(is_bouncy(121))

    n = 0
    bouncy_count = bouncy_percent = 0
    while True:
        n += 1
        print(n, is_bouncy(n))
        if is_bouncy(n):
            bouncy_count += 1
            bouncy_percent = bouncy_count / n * 100
            print("{}, {}%".format(n, bouncy_percent))
            if bouncy_percent == 99:
                print("Bouncy percent 99 at {} for n = {}".format(bouncy_count, n))
                break
        #n += 1

    print("Bouncy percent {} at {}".format(bouncy_percent, bouncy_count))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
