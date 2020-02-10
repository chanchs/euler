import lib.utilities as ut
import math
import time


if __name__ == "__main__":
    start = time.time()

    count = 0
    a = []

    for b in range(2, 100):
        for e in range(2, 50):
            n = int(math.pow(b, e))
            if ut.get_digital_sum(n) == b:
                count += 1
                a.append(n)
                if count > 30:
                    break

    print(a[30])

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
