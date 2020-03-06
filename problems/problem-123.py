import lib.utilities as ut
import time


if __name__ == "__main__":
    start = time.time()

    limit = 10000000000
    P = ut.primes_to(1000000)
    nP = p = d = r = 0
    l = len(P)
    for i in range(l):
        # print(i, P[i])
        nP = pow(P[i], i + 1)
        d = P[i] * P[i]
        if (i + 1) % 2 == 0:
            r = (2 * nP + 2) % d
        else:
            r = (2 * nP + 2 * (i + 1) * P[i]) % d
        if r > limit:
            break
    print(i + 1)


    print(p)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
