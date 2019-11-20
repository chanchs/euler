import lib.utilities as ut
import time


def count(n, s):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        num = len(s)
        if num == 0:
            return 0
        elif num == 1:
            return n % s[0] == 0
        else:
            return count(n, s[1:]) + count(n - s[0], s)


if __name__ == "__main__":
    start = time.time()

    n = 2
    while True:
        s = ut.primes_to(n)
        print(len(s), s)
        c = count(n, s)
        print("n = {}, partitions = {}".format(n, c))
        if c > 5000:
            break
        else:
            n += 1

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
