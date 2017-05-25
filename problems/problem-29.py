import math
import time


if __name__=="__main__":
    start = time.time()
    max = 100
    d = []
    count = 0
    for a in range(2, max + 1):
        for b in range(2, max + 1):
            n = math.pow(a, b)
            if n not in d:
                #d.append(n)
                count += 1
    print("numbers count = {}".format(count))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))