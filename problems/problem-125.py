import lib.utilities as ut
import math
import time


if __name__ == "__main__":
    start = time.time()

    max_num = 100000000
    total_sum = 0
    lst = []
    sqr_limit = int(math.sqrt(max_num))
    for i in range(1, sqr_limit + 1):
        n = i * i
        for j in range(i + 1, sqr_limit + 1):
            n += j * j
            if n > max_num:
                break
            if ut.is_palindrome(n) and n not in lst:
                print("-- {}".format(n))
                total_sum += n
                lst.append(n)

    print(total_sum)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
