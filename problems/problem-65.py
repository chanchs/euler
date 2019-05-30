import time

import lib.utilities as ut

if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    a = [0] * 100
    count = 0
    b = 2
    a[0] = 2

    for i in range(1, len(a)):
        if count == 1:
            a[i] = b
            b += 2
        else:
            a[i] = 1

        if count >= 2:
            count = 0
        else:
            count += 1

    h1 = 1
    h2 = 0
    k1 = 0
    k2 = 1
    hn = 0
    kn = 0

    for i in range(len(a)):
        hn = a[i] * h1 + h2
        kn = a[i] * k1 + k2
        print("i = {}, an = {}, h = {}, k = {} ".format(i, a[i], hn, kn))

        h2 = h1
        k2 = k1

        h1 = hn
        k1 = kn

    s = ut.get_digital_sum(hn)
    print("sum = {}".format(s))
    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))