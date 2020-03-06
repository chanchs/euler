import lib.utilities as ut
import math
from itertools import permutations
count = 0
end_numbers = [1, 3, 7, 9]
L = 4


def number(num):
    if num[0] == 0:
        return 0
    if num[-1] == 0:
        return 0
    n = 0
    for d in num:
        n = n * 10 + d
    if ut.is_prime(n, 4):
        return n
    else:
        return 0

if __name__ == "__main__1":
    a = [0] * L
    s = 0
    for fill_numbers in range(10):
        for k in range(L - 1):
            for i in range(10):
                a = [fill_numbers] * L
                a[k] = i
                sm = number(a)
                if sm > 0:
                    sm += s
                print(a, sm)
                count += 1
        print(fill_numbers, s)

    print(sm, count)


def partition_count(m):
    a = [0] * (m + 1)
    p = [1] * (m + 1)

    for u in range(2, m + 1):
        for i in range(m + 1):
            a[i] = p[i]
            p[i] = 0
        for j in range(0, m + 1, u):
            for k in range(j, m + 1):
                p[k] = p[k] + a[k - j]
    return p


def partition_count1(m):
    m = m + 1
    p = [1] * m
    for i in range(1, m):
        j = k = 1
        s = 0
        while j > 0:
            j = i - (3 * k * k + k) // 2
            if j >= 0:
                s = s - (-1) ** k * p[j]
            j = i - (3 * k * k - k) // 2
            if j >= 0:
                s = s - (-1) ** k * p[j]
            k = k + 1
        p[i] = s
    return p


def check_partitions(m):
    for i in range(len(m)):
        n = 0
        for j in range(i + 1):
            n = n * 10 + m[j]


def is_palindrome(n):
    """
    check if a number is palindrome, faster than above
    :param n: the number to be checked
    :return: true or false
    """
    d = int(math.pow(10, int(math.log10(n))))
    while n != 0:

        if 0 > n > 10:
            break
        leading = n // d
        trailing = n % 10
        if leading != trailing:
            return False
        n = (n % d) // 10
        d = d // 100
    return True


def create_palindrome(n, odd):
    p = n
    if odd:
        n = n // 10
    while n > 0:
        p = p * 10 + n % 10
        n = n // 10
    return p


def generate_palindromes(n):
    for j in range(2):
        i = 1
        while create_palindrome(i, j % 2) < n:
            yield create_palindrome(i, j % 2)
            i += 1


def dummy_function(x, y, z):
    return x * y * z


def test_loop():
    x = y = z = 1
    while dummy_function(z, z, z) < 1000:
        z += 1
        y = z
        while dummy_function(z, y, z) < 1000:
            y += 1
            x = y
            while dummy_function(z, y, x) < 1000:
                x += 1
                print("x = {}, y = {}, z = {}, dummy_function = {}".format(x, y, z, dummy_function(z, y, x)))


def test_loop1():
    x = y = z = 1
    for x in range(1, dummy_function(x, y, z)):
        x += 1
        y += 1
        z += 1
        print("hello")


if __name__ == "__main__":
    print(ut.nCr(9, 0))
    s = 0
    #for n in range(8):
    #    s = s + ut.nCr(9, n)

    print(ut.nCr(7, 4))
    print(ut.nPr(7, 4))
    print(partition_count(7))
    print(partition_count1(7))
    p1 = ut.primes_to(10)
    p2 = ut.primes_to(999)
    #p3 = ut.primes_to(9999)
    #p4 = ut.primes_to(99999)
    #p5 = ut.primes_to(999999)
    #p6 = ut.primes_to(9999999)
    #p7 = ut.primes_to(99999999)
    print(ut.primes_to(100))
    print(len(p1))
    print(len(p2) - len(p1))
    s = 1
    for i in range(7):
        s *= math.factorial(i)
    print(s)
    #print(len(p3) - len(p2))
    #print(len(p4) - len(p3))
    #print(len(p5) - len(p4))
    v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #x = permutations(v, 9)

    #for p in x:
    #    print(p)
    print("is 1234567890 palindrome? {}".format(is_palindrome(1234567890)))
    print("is 123454321 palindrome? {}".format(is_palindrome(123454321)))
    print("is 12344321 palindrome? {}".format(is_palindrome(12344321)))
    print("is 91 * 99 palindrome? {}".format(is_palindrome(91 * 99)))
    print("is 1 palindrome? {}".format(is_palindrome(1)))
    print("is 11 palindrome? {}".format(is_palindrome(11)))
    print("is 101 palindrome? {}".format(is_palindrome(101)))
    print("is 111 palindrome? {}".format(is_palindrome(111)))
    print("is 1001 palindrome? {}".format(is_palindrome(1001)))
    print("is 1 palindrome? {}".format(is_palindrome(1)))
    print("is 2 palindrome? {}".format(is_palindrome(2)))
    print("is 5 palindrome? {}".format(is_palindrome(5)))
    print("is 7 palindrome? {}".format(is_palindrome(7)))
    print("is 9 palindrome? {}".format(is_palindrome(9)))
    for p in generate_palindromes(10):
        print(p)
    #test_loop()
    #test_loop1()
    r = 100 * [1]
    print(r)
    for i in range(2, 100):
        if r[i] == 1:
            r[i] = i

            for j in range(i + i, 100, i):
                r[j] *= i

    print(r)
