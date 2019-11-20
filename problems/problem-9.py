import lib.utilities as ut
import math
import time

if __name__=="__main__":
    start = time.time()
    a = b = c = s = p = 0
    m = k = n = d = 0
    lt = 1000
    lt_2 = lt / 2
    done = False

    limit = int(math.sqrt(lt / 2))

    for m in range(2, limit):
        if lt_2 % m == 0:
            if m %2 ==0:
                k = m + 1
            else:
                k = m + 2
        while k < 2 * m and k <= lt_2 / m:
            if (lt_2 / m) % k == 0 and ut.gcd_recursive(k, m) == 1:
                d = lt_2 / (k * m)
                n = k - m
                a = d * (m**2 - n**2)
                b = 2 * d * n * m
                c = d * (m**2 + n**2)
                done = True
                break
            k += 2
        if done:
            break
    end = time.time()

    print("a = {0}, b = {1}, c= {2}, p = {3}, s = {4}".format(a, b, c, a*b*c, a+b+c))
    print("Completed in {0:.2}s".format(end - start))