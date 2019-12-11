import lib.utilities as ut
import math
import time


# this solution is one of the solutions in the problems discussion page. Not faster than my solution. Did not delete
# this as I took the trouble to type it. Use my solution.. runs in about 5 minutes
if __name__ == "__main__1":
    start = time.time()
    p_limit = 1000000000
    count = 0

    for i in range(3, p_limit // 3, 2):
        if ut.is_square(i * i - (i - 1) * (i - 1) / 4):
            count += 3 * i - 1
            print("found i = {}, b = {}".format(i, i - 1))
        if ut.is_square(i * i - (i + 1) * (i + 1) / 4):
            count += 3 * i + 1
            print("found i = {}, b = {}".format(i, i + 1))
    print("sum = {}".format(count))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))


if __name__ == "__main__":
    start = time.time()

    a = b = c = m = n = count = p = k = 0
    a1 = b1 = c1 = 0
    p_limit = 1000000000
    limit = int(math.sqrt(p_limit))
    print(limit)
    P = []
    for m in range(1, limit):
        for n in range(1, m):  # because n < m
            # m and n are of opposite parity and co-prime
            if math.gcd(m, n) == 1 and ((m % 2 == 0 and n % 2 != 0) or (m % 2 != 0 and n % 2 == 0)):
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                key = False
                k = 1
                while not key:
                    a1 = a * k
                    b1 = b * k
                    c1 = c * k
                    p = 2 * k * m * (m + n)
                    if p <= p_limit and (c1 == 2 * a1 + 1 or c1 == 2 * a1 - 1 or c1 == 2 * b1 + 1 or c1 == 2 * b1 - 1):
                        key = False
                        per = 0
                        if c1 == 2 * a1 + 1 or c1 == 2 * a1 - 1:
                            per = 2 * c1 + 2 * a1
                        if c1 == 2 * b1 + 1 or c1 == 2 * b1 - 1:
                            per = 2 * c1 + 2 * b1
                        count += per
                        k += 1
                        print("L = {}, b = {}, h = {}, Perimeter = {}".format(c1, 2 * a1, b1, per))
                        P.append(per)
                    else:
                        key = True
    print("Total count = {}, sum of perimeters = {}".format(len(P), count))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
