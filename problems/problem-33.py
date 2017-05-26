import time
import lib.utilities as ut


if __name__=="__main__":
    start = time.time()
    den, num = 1, 1
    for n in range(10, 100):
        for d in range(10, 100):
            if n / d < 1:
                n1 = int(n / 10)
                n2 = n % 10
                d1 = int(d / 10)
                d2 = d % 10
                if d and d2 != 0:
                    if n2 == d1 and (n1 / d2) == (n / d):
                        print("n1 = {0}, n2 = {1}, d1 = {2}, d2 = {3}".format(n1, n2, d1, d2))
                        print("{0} / {1} = {2}".format(n1, d2, n1/d2))
                        num *= n1
                        den *= d2
    print("{0} / {1}".format(num, den))
    g = ut.gcd_recursive(num, den)
    print("{0} / {1}".format(num/g, den/g))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))