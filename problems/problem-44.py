import time
import lib.utilities as ut

if __name__=="__main__":
    start = time.time()
    E = False
    i = 1
    result = 0
    while E is False:
        i += 1
        n = int(i * (3 * i - 1) / 2)
        for j in range(i - 1, 0, -1):
            m = int(j * (3 * j -1) / 2)
            if ut.is_pentagonal(n + m) and ut.is_pentagonal(n - m):
                result = n - m
                E = True
                break
    print("result = {}".format(result))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
