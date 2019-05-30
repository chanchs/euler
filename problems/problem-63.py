import time
import math


if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    count = 0
    for b in range(1, 10):
        for e in range(1, 101):
            number = b ** e
            l = int(math.log10(number)) + 1
            if l == e:
                count += 1
                print("number = {}, base = {}, exponent = {}".format(number, b, e))

    print("Total count = {}".format(count))

    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))
