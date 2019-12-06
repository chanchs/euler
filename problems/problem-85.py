import lib.utilities as ut
import time


if __name__ == "__main__":
    start = time.time()
    target = 2000000
    x = 200
    y = 1
    error = 100000000

    while x >= y:
        rects = ut.binomial(x + 1, 2) * ut.binomial(y + 1, 2)
        print("x = {}, y = {}, Rects = {}".format(x, y, rects))
        if error > abs(rects - target):
            area = x * y
            closex= x
            closey = y
            error = abs(rects - target)
        if rects > target:
            x -= 1
        else:
            y += 1
    print("area = {}, for x = {} and y = {}".format(area, x, y))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
