import math
import time
import lib.utilities as ut


def have_same_digits(x):
    a = x
    b = 2 * x
    c = 3 * x
    d = 4 * x
    e = 5 * x
    f = 6 * x
    digits = [0] * 10
    la = int(math.log10(a)) + 1
    lb = int(math.log10(b)) + 1
    lc = int(math.log10(c)) + 1
    ld = int(math.log10(d)) + 1
    le = int(math.log10(e)) + 1
    lf = int(math.log10(f)) + 1

    if (la == lb) and (lb == lc) and (lc == ld) and (ld == le) and (le == lf):
        for i in range(la):
            digits[a % 10] += 1
            digits[b % 10] -= 1

            digits[c % 10] += 1
            digits[d % 10] -= 1

            digits[e % 10] += 1
            digits[f % 10] -= 1

            a = int(a / 10)
            b = int(b / 10)

            c = int(c / 10)
            d = int(d / 10)

            e = int(e / 10)
            f = int(f / 10)
    else:
        return False
    return all(dg == 0 for dg in digits)



if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    a = 125874
    b = 251748

    print(have_same_digits(a))
    E = False
    i = 0
    while not E:
        i += 1
        #print(i)
        if have_same_digits(i):
            print("Answer = {0}, {1}, {2}, {3}, {4}, {5}".format(i, 2 * i, 3 * i, 4 * i, 5 * i, 6 * i))
            E = True
            break

    end = time.time()
    print("Ending......")
    print("Completed in {0:.2}s".format(end - start))