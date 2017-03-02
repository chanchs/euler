import lib.utilities as ut
import time

if __name__=="__main__":
    start = time.time()
    large = 0
    large_d1 = 0
    large_d2 = 0
    for d1 in range(100, 1000):
        for d2 in range(d1, 1000):
            product = d1 * d2
            if ut.is_palindrome(product) and (product > large):
                large = product
                large_d1 = d1
                large_d2 = d2

    end = time.time()

    print("Finished in {0:.2}s".format(end-start))
    print("{0} x {1} = {2}".format(d1, d2, large))