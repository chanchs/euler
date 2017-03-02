import lib.utilities as ut
import time

if __name__=="__main__":
    start = time.time()
    big = 0
    start_no = 0
    n = 1000000
    while n > 2:
        n -= 1
        s, t = ut.collatz_sequence(n)
        print("index = {0}, size = {1}".format(n, t))
        if t > big:
            big = t
            start_no = n
    print("largest sequence has {0} terms and starting number is {1}".format(big, start_no))
    end = time.time()
    print("Completed in {0:.2}".format(end - start))