import lib.utilities as ut
import time


def A(n):
    if ut.gcd(n, 10) != 1:
        return 0
    x = 1
    k = 1
    while x != 0:
        x = (x * 10 + 1) % n
        k += 1
    return k


if __name__ == "__main__":
    start = time.time()

    limit = 25
    f = 0
    n = 1
    result = 0

    while f < limit:
        n += 1
        if ut.is_prime1(n):
            continue
        a = A(n)

        if a != 0 and (n - 1) % a == 0:
            result += n
            f += 1
    print(limit, result)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
