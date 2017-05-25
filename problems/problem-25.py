import math
import time


if __name__=="__main__":
    start = time.time()

    F1 = 1
    F2 = 1
    next_num = 0
    l = 0
    term = 2
    while l < 1000:
        next_num = F1 + F2
        l = int(math.log(next_num, 10) + 1)
        F1 = F2
        F2 = next_num
        print("\n{}".format(next_num))
        term += 1
    print("term : {0}, digits : {1}".format(term, int(math.log(next_num) + 1)))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))