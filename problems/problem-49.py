import math
import time
import lib.utilities as ut

def is_permutation(n1, n2):
    if n1 == n2:
        return False
    l1 = int(math.log10(n1)) + 1
    d1 = []
    d2 = []
    for k in range(l1):
        d1.append(int(n1 % 10))
        n1 = int(n1 / 10)
        d2.append(int(n2 % 10))
        n2 = int(n2 / 10)
    d1.sort()
    d2.sort()
    if d1 == d2:
        return True
    else:
        return False

if __name__ == "__main__":
    start = time.time()

    p = ut.n_primes(1230)
    p4 = [x for x in p if int(math.log10(x) + 1) == 4]
    print(p4)
    l = len(p4)
    for i in range(l):
        for j in range(i, l):
            d = p4[j] - p4[i]
            n = p4[j] + d
            if n in p4 and is_permutation(p4[i], p4[j]) and is_permutation(p4[j], n):
                    print("{0}, {1}, {2}".format(p4[i], p4[j], n))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
