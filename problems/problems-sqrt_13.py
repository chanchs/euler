import lib.utilities as ut
import math
import time

if __name__ == "__main__":
    start = time.time()
    result = ut.digit_by_digit_sqrt(2, 100)
    print(result, type(result))
    d = result.split('.')
    s = 0
    for digit in d[1]:
        s += int(digit)
    print(s)

    result = ut.digit_by_digit_sqrt(13, 1000)
    print(result, type(result))
    d = result.split('.')
    s = 0
    for digit in d[1]:
        s += int(digit)
    print(s)


    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

