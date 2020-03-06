import lib.utilities as ut
import time


def A(n):
    if ut.gcd1(n, 10) != 1:
        return 0
    x = k = 1
    while x != 0:
        x = (x * 10 + 1) % n
        k += 1
    return k


if __name__ == "__main__":
    print("Starting....")
    start = time.time()
    print("A(7) = {}".format(A(7)))
    print("A(41) = {}".format(A(41)))

    limit = 1000001
    n = limit
    while A(n) < limit:
        n += 2
    print(n)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
