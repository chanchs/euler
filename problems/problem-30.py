import math
import time


if __name__=="__main__":
    start = time.time()

    exp = 5
    s = 0
    ts = 0
    for number in range(1, 1000000):
        s = 0
        n = number
        #print(number)
        for i in range(0, int(math.log(number))):
            d = n % 10
            s += d * d * d * d * d
            n = int(n / 10)
            #print("s = {0}, d^4 = {1}".format(s, d^4))
        #print(s)
        if s == number:
            print(number)
            ts += s
    print("total = {}".format(ts))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))