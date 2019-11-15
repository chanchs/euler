from lib.utilities import gcd
import time


if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    N = 12000
    count = 0
    for d in range(1, N + 1):
        for n in range(1, d):
            if 3 * n > d > 2 * n:
                if gcd(n, d) == 1:
                    print("{} / {}".format(n, d))
                    count += 1
    print("count = {}".format(count))
    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))
