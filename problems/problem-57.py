import math
import time
import lib.utilities as ut


if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    counter = 0

    nMi = 7
    nM2i = 3

    dMi = 5
    dM2i = 2

    for i in range(1, 1000 - 2):
        N = 2 * nMi + nM2i
        D = 2 * dMi + dM2i

        nM2i = nMi
        nMi = N

        dM2i = dMi
        dMi = D

        if int(math.log10(N)) > int(math.log10(D)):
            counter += 1
            print(counter)


    end = time.time()
    print("Ending......")
    print("Completed in {0:.2}s".format(end - start))