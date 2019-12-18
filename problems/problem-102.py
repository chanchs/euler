import math
import time
import lib.utilities as ut


def contains_origin(v0, v1, v2):
    v = [0, 0]
    v1_X_v2 = ut.cross_product(v1, v2)
    a = (ut.cross_product(v, v2) - ut.cross_product(v0, v2)) / v1_X_v2
    b = -(ut.cross_product(v, v1) - ut.cross_product(v0, v1)) / v1_X_v2
    if (a > 0 and b > 0) and (a + b) < 1:
        return True
    else:
        return False


if __name__ == "__main__":
    start = time.time()

    origins = 0
    non_origin = 0
    lines = 0
    with open("problem-102.txt") as f:
        for line in f:
            v0 = [0] * 2
            v1 = [0] * 2
            v2 = [0] * 2
            v = [int(x) for x in list(line.strip().split(","))]
            #print(v)
            v0[0] = v[0]
            v0[1] = v[1]
            v1[0] = v[2] - v0[0]
            v1[1] = v[3] - v0[1]
            v2[0] = v[4] - v0[0]
            v2[1] = v[5] - v0[1]
            lines += 1
            if contains_origin(v0, v1, v2):
                print("Triangle {} has origin inside".format(lines))
                origins += 1
            else:
                print("Triangle {} does not have origin inside".format(lines))
                non_origin += 1
    f.close()
    print("Inside origin = {}, outside = {}".format(origins, non_origin))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
