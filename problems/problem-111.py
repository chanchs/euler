import lib.utilities as ut
import time


def number(num):
    if num[0] == 0:
        return 0
    if num[-1] == 0:
        return 0
    n = 0
    for d in num:
        n = n * 10 + d
    if ut.is_prime(n, 4):
        #print(num, n, True)
        return n
    else:
        #print(num, n, False)
        return 0


def cycle_numbers(n, length):
    s = 0
    for d in range(10):
        for i in range(length):
            num = [n] * length
            num[i] = d
            sm = number(num)
            if sm > 0:
                # print(num, sm, s)
                s += sm
    return s


def cycle_numbers1(n, length):
    end_numbers = [1, 3, 7, 9]
    s = 0
    for d in range(10):
        for i in range(length - 1):
            for e in end_numbers:
                num = [n] * length
                num[length - 1] = e
                num[i] = d
                #print(num)
                s += number(num)

    return s


if __name__ == "__main__":
    start = time.time()
    s = 0
    digits = 10

    # cycle through 1 to 9, 0 is a special case
    for d in range(0, 10):
        sm = cycle_numbers(d, digits)
        if sm == 0:
            sm = cycle_numbers1(d, digits)
        print(sm, d)
        s += sm
    print("s({}, d) = {}".format(digits, s))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
