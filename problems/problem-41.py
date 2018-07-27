import math
import time
import lib.utilities as ut


if __name__=="__main__":
    start = time.time()

    # 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45 % 3 = 0
    # 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 36 % 3 = 0
    n = 9876543
    #n = 3001
    answer = 0
    for i in range(n, 0, -2):
        ld = i % 10
        if ld not in [2, 4, 5, 6, 8, 0]:
            #print("{} does not have [2, 4, 6, 8 or 0] as last digit".format(i))
            if ut.is_n_pandigital(i):
                #print("{} is n pandigital".format(i))
                if ut.is_prime(i):
                    print("{} is prime".format(i))
                    answer = i
                    break
    print(answer)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
