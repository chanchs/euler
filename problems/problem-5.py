import utility as ut
import math
import time

if __name__ == "__main__":
    start = time.time()

    n = 2520
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # 1, 2, 3, 2 * 2, 5, 2 *3, 7, 2*2*2, 3 * 3, 2 * 5
    # 1, 2, 2, 2, 3, 5, 7, 3

    print(1 * 2 * 2 * 2 * 3 * 5 * 7 * 3)
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

    new_n = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 2 * 3 * 2 * 2 * 1
    print("new n = {}".format(new_n))


    end = time.time()

    print("Completed in {0:.2}s".format(end - start))