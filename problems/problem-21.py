import lib.utilities as ut
import time

if __name__ == "__main__":

    start = time.time()
    n = 0
    for a in range(1, 10000):
        f1, b = ut.factor(a)
        #print(b)
        f2, a_ = ut.factor(b)
        #print(a_)
        if a == a_ and b != a:
            print("hello")
            n += a

    print("numbers = {}".format(n))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
