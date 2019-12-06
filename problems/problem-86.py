import lib.utilities as ut
import math
import time

# s = sqrt(l*l + (w + h) * (w + h))
# w + h = wh


if __name__ == "__main__":
    start = time.time()
    l = 2
    count = 0
    limit = 1000000
    while count < limit:
        l += 1
        for wh in range(3, 2 * l + 1):
            if math.sqrt(wh * wh + l * l).is_integer():
                if wh <= l:
                    count += wh / 2
                    #print(wh, l, count)
                else:
                    count += 1 + (l - (wh + 1) / 2)
                    #print(wh, l, count)
    print("count = {}, wh = {}, l = {}".format(count, wh, l))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
