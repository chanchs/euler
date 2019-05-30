import time
import math

if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    odd_period_count = 0
    for s in range(10001):
        m = 0
        d = 1
        print("s = {} : ".format(s), end=" ")
        a0 = a = math.floor(math.sqrt(s))
        key = False
        print("a0 = {} : ".format(a0), end=" ")

        if a0 * a0 != s:
            period = 0

            while not key:
                m = d * a - m
                d = (s - m * m) /d
                a = math.floor((a0 + m) / d)
                print(", {}".format(a), end=" ")
                period += 1
                if 2 * a0 == a:
                    key = True
            print(": Period = {}".format(period))

            if period % 2 != 0:
                odd_period_count += 1

    print("Total number with odd periods : {}".format(odd_period_count))
    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))