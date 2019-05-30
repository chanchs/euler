import math


def matrix_multiply(A, B):
    """
    :param A: first matrix 
    :param B: second matrix
    :return: product of A * B
    """
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
    """
    :param size: size of identity matrix to return 
    :return: an identity matrix of size n
    """
    size = range(size)
    return [[(i == j) * 1 for i in size] for j in size]


def matrix_exponentiation(M, n):
    """
    :param M: Matrix 
    :param n: exponent
    :return: a matrix raised to n
    """
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
    return P, sorted({k: v for k, v in enumerate(P) if v is True})


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
    elif n < 0:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    elif n % 5 == 0:
        return False
    else:
        r = int(math.floor(math.sqrt(n)))
        d = 5
        while d <= r:
            if n % d == 0:
                return False
            if n % (d + 2) == 0:
                return False
            d += 6
    return True


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


def n_primes(n):
    """
    return n primes starting from 2
    :param n: the number of primes to return
    :return: returns a list of primes
    """
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


def is_palindrome(n):
    """
    check if a number is palindrome
    :param n: the number to be checked
    :return: true or false
    """
    l = int(math.log10(n))
    num = n
    p = 0
    for i in range(l, -1, -1):
        p += int((num % 10)) * int(math.pow(10, i))
        num = num // 10
    if int(p) == int(n):
        return True
    else:
        return False


def gcd_iterative(u, v):
    """
    This guy has a bug
    :param u: 
    :param v: 
    :return: 
    """
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


def generate_triangle_numbers(n):
    tn = [0] * (n + 1)
    for i in range(n + 1):
        tn[i] = int(0.5 * i * (i + 1))
    return tn


def calculate_weight(word):
    alphabet = {'A': 1,
                'B': 2,
                'C': 3,
                'D': 4,
                'E': 5,
                'F': 6,
                'G': 7,
                'H': 8,
                'I': 9,
                'J': 10,
                'K': 11,
                'L': 12,
                'M': 13,
                'N': 14,
                'O': 15,
                'P': 16,
                'Q': 17,
                'R': 18,
                'S': 19,
                'T': 20,
                'U': 21,
                'V': 22,
                'W': 23,
                'X': 24,
                'Y': 25,
                'Z':26}
    weight = 0
    for i in range(len(word)):
        weight += alphabet[word[i]]
    return weight


def factor(n):
    ff = []
    lim = int(math.sqrt(n)) + 1
    ff.append(1)
    for d in range(2, lim):
        if n % d == 0:
            ff.append(int(n / d))
            ff.append(d)
    ff.sort()
    return ff, sum(ff)


def prime_factors(n, sorted=False, distinct=True):
    limit = (int)(math.sqrt(n)) + 1
    p = n_primes(limit)
    if is_prime(n):
        return [n]
    ff = []
    if n % p[0] == 0:
        ff.append(p[0])
        n = int(n / p[0])
        if n in p:
            ff.append(n)
    for primes in p:
        if n % primes == 0 and primes not in ff:
            ff.append(primes)
            n = int(n / primes)
            if n in p and (n not in ff != distinct):
                ff.append(n)
    if sorted:
        ff.sort()
    return ff


def is_pandigital(n):
    l = int(math.log(n, 10) + 1)
    s = [False] * 10
    if l > 9:
        return False
    number = n
    #print("n = {0}, l = {1}".format(n, l))
    for i in range(l):
        digit = n % 10
        n = int(n / 10)
        #print(digit)
        if not s[digit]:
            s[digit] = True
        else:
            return False
    #print("number = {0}, s = {1}".format(number, s))
    if False in s[1:]:
        return False
    else:
        return True


def is_09_pandigital(n):
    l = int(math.log(n, 10) + 1)
    s = [False] * 10
    if l > 10:
        return False
    number = n
    #print("n = {0}, l = {1}".format(n, l))
    for i in range(l):
        digit = n % 10
        n = int(n / 10)
        #print(digit)
        if not s[digit]:
            s[digit] = True
        else:
            return False
    #print("number = {0}, s = {1}".format(number, s))
    if False in s:
        return False
    else:
        return True


def is_pentagonal(n):
    N = (1 + math.sqrt(1 + 24 * n)) / 6
    if N == int(N):
        return True
    else:
        return False


def is_n_pandigital(n):
    """
    :param n: integer
    :return: True if the number is n pandigital, false otherwise
    """
    l = int(math.log10(n) + 1)
    s = [False] * (l + 1)
    if l > 9:
        return False
    for i in range(l):
        digit = n % 10
        n = int(n / 10)
        if digit > l:
            return False
        if digit == 0:
            return False
        if not s[digit]:
            s[digit] = True
        else:
            return False
    if False in s[1:]:
        return False
    else:
        return True


def get_digits(n, sorted=False):
    """
    :param n: number 
    :return: returns the digits in number in revered order
    """
    s = []
    l = int(math.log(n,10) + 1)
    for i in range(l):
        s.append(n % 10)
        n = int(n / 10)
    if sorted:
        s.sort()
    return s


def reverse(n):
    l = int(math.log10(n)) + 1
    m = 0
    for i in range(l):
        d = n % 10
        n = int(n / 10)
        m = m * 10 + d
    return m


def rotate(n, ln):
    """
    :param n: the number to rotate 
    :param ln: the log of the number (number of digits in the number)
    :return: the number roatated (e.g.,  197, 971, and 719)
    """
    if not ln:
        ln = int(math.log(10, n))
    last = n % 10
    mid = (n - last) / 10
    rvalue = last * math.pow(10, ln) + mid
    return int(rvalue)


def convert_decimal_to_binary(n):
    """
    :param n: decimal number 
    :return: binary (under a million)
    """
    b, num, iteration, num_2 = 0, 0, 0, 0
    num = n
    while num != 0:
        num_2 = num % 2
        #print("num = {0}, num_2 = {1}, iteration = {2}".format(num, num_2, iteration))
        b += int(num_2 * math.pow(10, iteration))
        num = int(num / 2)
        iteration += 1
    return b


def nCr(n, r):
    if r > n:
        temp = r
        r = n
        n = temp
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


def unique_partitions(n):
    p = [[]]
    row = 0
    k = 0
    p[row].append(n)
    while True:
        print(p)
        remaining_value = 0
        print("row = {0} k = {1}".format(row, k))
        while k >= 0 and p[row][k] == 1:
            remaining_value += p[row][k]
            k -= 1
        if k < 0:
            return
        p[row][k] -= 1
        remaining_value += 1
        while remaining_value > p[row][k]:
            p[row].append(p[k])
            k += 1
            remaining_value = remaining_value - p[row][k]
            #k += 1
        p[row].append(remaining_value)
        k += 1
        row += 1


def get_nth_digit(n, position):
    """
    :param n: number (integer)
    :param position: position to return
    :return: integer at position
    """
    return n // 10**(int(math.log10(n) + 1) - position) % 10


def get_digital_sum(n):
    """
    :param n: number
    :return: returns the digits in number in revered order
    """
    if n == 0:
        return 0
    s = 0
    l = int(math.log(n) + 1)
    for i in range(l):
        s += (n % 10)
        n = n // 10   # integer division, fixes division of large numbers
    return s


if __name__=="__main__":
    print("hello world")
    print(n_th_fibonacci(12))
    [print(i) for i in fibonacci_generative_to_n(9)]
    primes, P = sieve_of_eratosthenes(10)
    print(primes)
    print(P)
    #for i in P:
    #    print(i)
    print("is 1234567890 verome? {}".format(is_palindrome(1234567890)))
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
    print(n_primes(6))
    print(collatz_sequence(13))
    f, s = factor(16)
    print("f = {0}, s= {1}".format(f, s))
    f, s = factor(284)
    print("f = {0}, s= {1}".format(f, s))
    print("is prime(4) {}".format(is_prime(4)))
    print("is prime(2) {}".format(is_prime(2)))
    print("is prime(3) {}".format(is_prime(3)))
    print("is_prime(1761) {}".format(is_prime(1761)))
    print("is_pandigital(123456789) {}".format(is_pandigital(123456789)))
    print("is_pandigital(8372377817263) {}".format(is_pandigital(8372377817263)))
    print("is_pandigital(3474002) {}".format(is_pandigital(3474002)))
    print("is_pandigital(987654321) {}".format(is_pandigital(987654321)))
    print("{}".format(get_digits(123456789)))
    print("{}".format(get_digits(8372377817263)))
    print("{}".format(get_digits(3474002)))
    print("{}".format(get_digits(987654321)))
    print(convert_decimal_to_binary(1000000))
    print(convert_decimal_to_binary(585585))
    print(is_palindrome(convert_decimal_to_binary(585585)))
    #print("partition of 2 {}".format(unique_partitions(2)))
    #print("partition of 2 {}".format(unique_partitions(3)))
    #print("partition of 2 {}".format(unique_partitions(4)))
    print("12th digit of 125487956395214789 = {}".format(get_nth_digit(1234567890, 4)))
    print("1st digit of 125487956395214789 = {}".format(get_nth_digit(1234567890, 1)))
    print("2nd digit of 125487956395214789 = {}".format(get_nth_digit(1234567890, 2)))
    print("is_n_pandigital(12345) {}".format(is_n_pandigital(12345)))
    print("is_n_pandigital(123045) {}".format(is_n_pandigital(123045)))
    print("is_n_pandigital(523641) {}".format(is_n_pandigital(523641)))
    print("is_n_pandigital(1234567890123456789) {}".format(is_n_pandigital(1234567890123456789)))
    print("is_09_pandigital(9012384756) {}".format(is_09_pandigital(9012384756)))
    print("is_09_pandigital(9012384765) {}".format(is_09_pandigital(9012384765)))
    print("is_09_pandigital(901256) {}".format(is_09_pandigital(901256)))
    print(get_digital_sum(546812681195752981093125556779405341338292357723303109106442651602488249799843980805878294255763456))
