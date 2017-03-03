import math


def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Cannot multiply matrices")
        return

    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    #print(C)

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C


def identity(size):
    size = range(size)
    return [[(i == j) * 1 for i in size] for j in size]


def matrix_exponentiation(M, n):
    assert n >= 0 and int(n) == n, "power has to be non-negative integer"
    if(n == 0 or n == 1):
        return
    A = identity(len(M))
    for i in range(n):
        A = matrix_multiply(A, M)
    return A


def n_th_fibonacci(n):
    # http://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
    # [1 1; 1 0]^n = (Fn+1 Fn; Fn Fn-1)
    # nth Fibonacci
    F = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    R = matrix_exponentiation(F, n-1)
    return R[0][0]


def fibonacci_generative_to_n(n):
    a, b = 0, 1
    while n>0:
        yield a
        a, b, n = b, a+b, n-1


def sieve_of_eratosthenes(n):
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes  # Algorithm_and_variants
    P = [True for i in range(n+1)]
    P[0] = P[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if P[i]:
            for j in range(i*i, n+1, i):
                P[j] = False

    return P, sorted({k: v for k, v in enumerate(P) if v == True})


def is_prime(n):
    """
    1 is not a prime
    All primes except 2 are odd
    All primes greater than 3 can be written as 6k+/-1
    Any number n can have only one prime factor greater than sqrt(n)
    :param n:
    :return: True or false based on if n is a prime or not
    """
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 ==0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5

        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6

    return True


def n_primes(n):
    p = []
    p.append(2)
    p.append(3)

    m = p[-1]
    while True:
        if len(p) >= n:
            break
        m += 2
        limit = int(math.sqrt(m))
        i = 0
        is_prime = True
        while p[i] <= limit:
            if m % p[i] == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            p.append(m)

    return p


def is_palindrome(a):
    # limit to 32 bit integers for now
    l = int(math.log10(a)) + 1
    n = []

    for i in range(0, l):
        d = a % 10
        # if the last digit is 0, return false (0123210 = 123210)
        if i == 0 and d == 0:
            return False
        n.append(d)
        a = int(a / 10)
    if n[:] == n[::-1]:
        return True
    else:
        return False


def gcd_iterative(u, v):
    shift = 0
    if u == 0:
        return v
    if v == 0:
        return u

    for shift in range(0, (u | v) & 1):
        u >>= 1
        v >>= 1

    while u & 1 == 0:
        u >>= 1

    while v != 0:
        while v & 1 == 0:
            v >>= 1

        if u > v:
            t = v
            v = u
            u = t

        v = v - u

    return u << shift


def gcd_recursive(u, v):
    if u == v:
        return u

    if u == 0:
        return v

    if v == 0:
        return u

    if ~u & 1:
        if v & 1:
            return gcd_recursive(u >> 1, v)
        else:
            return gcd_recursive(u >> 1, v >> 1) << 1

    if ~v & 1:
        return gcd_recursive(u, v >> 1)

    if u > v:
        return gcd_recursive((u -v ) >> 1, v)

    return gcd_recursive((v - u) >> 1, u)


def collatz_sequence(n):
    s = []
    s.append(n)
    while n != 1:
        if ~n & 1:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        s.append(n)
    return s, len(s)


def binomial(n, k):
    p = 1
    for i in range(1, k + 1):
        p *= (n + 1 - i)
        p = int(p / i)
    return p


def big_pow(b, e):
    n = []
    n.append(1)
    for i in range(e):
        carry = 0
        for index in range(len(n)):
            number = n[index] * b + carry
            if number < 10:
                n[index] = number
                carry = 0
            else:
                n[index] = number % 10
                carry = int(number / 10)
        if carry > 0:
            n.append(carry)
    return list(reversed(n))


def factor(n):
    ff = []
    lim = int(math.sqrt(n))
    ff.append(1)
    for d in range(2, lim):
        if n % d == 0:
            ff.append(int(n / d))
            ff.append(d)
    ff.sort()
    return ff, sum(ff)


if __name__=="__main__":
    print("hello world")
    print(n_th_fibonacci(12))
    [print(i) for i in fibonacci_generative_to_n(9)]
    primes, P = sieve_of_eratosthenes(10)
    print(primes)
    print(P)
    #for i in P:
    #    print(i)
    print("is 1234567890 palindrome? {}".format(is_palindrome(1234567890)))
    #print("is 123454321 palindrome? {}".format(is_palindrome(123454321)))
    #print("is 12344321 palindrome? {}".format(is_palindrome(12344321)))
    #print("is 91 * 99 palindrome? {}".format(is_palindrome(91 * 99)))
    print(n_primes(6))
    print(collatz_sequence(13))
    f, s = factor(16)
    print("f = {0}, s= {1}".format(f, s))
    f, s = factor(284)
    print("f = {0}, s= {1}".format(f, s))