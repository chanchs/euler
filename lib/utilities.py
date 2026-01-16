import math
import random


def power_set(members):
    """
    :param members:
    :return:
        (tuple OR set OR list) -> list of sets

    Takes members, which is a tuple, set, or list representing the elements of
    the set for which a power set is desired. Populates a list with all the
    subsets of the group of members including the null set. Returns this list
    of sets.

    Note: in Python creating sets of sets is complicated and requires ordered
        sets, so this implementation actually returns a list of sets, not a
        set of sets.
    """
    subsets = [[]]
    for member in members:
        subsets.extend([subset + [member] for subset in subsets])
    return [set(x) for x in subsets]  # Converts to list of sets.


def has_unique_subset_sums(members):
    """
    (tuple OR set OR list) -> bool

    Takes members, which is a tuple, set, or list representing the elements of
    the set for which we would like to know if all subset sums are unique. The
    parameter members will henceforth be referred to as a set for convenience.
    Returns True if the number of non-empty subsets of members is equal to the
    number of elements in a set containing the sum of each subset. Returns
    False if the lengths differ, as this implies that at least two subsets
    have the same sum.

    :param members:
    :return:
    """

    # Lists all subsets of members and removes the null set from consideration:
    subsets = power_set(members)
    del subsets[0]  # We are interested only in non-empty subsets.

    # Creates a set containing the sums of all the subsets of members:
    sums = set(sum(subset) for subset in subsets)
    return len(sums) == 2 ** len(members) - 1


def has_duplicates(members):
    """
    (tuple OR list) -> bool

    Takes members, which is a tuple or list representing the elements of the
    set for which a power set is desired. The parameter members will
    henceforth be referred to as a set for convenience. Returns True if
    members contains no duplicate values. Returns False otherwise.

    :param members:
    :return:
    """

    if len(members) != len(set(members)):
        return True
    else:
        return False


def is_special_sum_set(members):
    """
    (tuple OR set OR list) -> bool

    Takes members, which is a tuple, set, or list representing the elements of
    the set for which a power set is desired. The parameter members will
    henceforth be referred to as a set for convenience. Returns True only if
    these two conditions both hold:
        1. The sum of each subset of members is unique. This is checked by
            the function has_unique_subset_sums; and,
        2. For any non-empty, disjoint subsets B and C, if B has more elements
            than C, then sum(B) > sum(C).

    Returns False otherwise.
    :param members:
    :return:
    """
    if (has_unique_subset_sums(members) and
        larger_subsets_have_larger_sums(members)):
            return True
    else:
        return False


def larger_subsets_have_larger_sums(members):
    """
    (tuple OR set OR list) -> bool

    Takes members, which is a tuple, set, or list representing the elements of
    the set for which a power set is desired. The parameter members will
    henceforth be referred to as a set for convenience. Checks that for any
    non-empty, disjoint subsets B and C, if B has more elements than C, then
    sum(B) > sum(C). Returns True if this condition holds. Returns False
    otherwise.

    This condition is checked by comparing extreme cases: we consider every
    possible pair of disjoint subset sizes n and n - 1 for 1 < n. For each
    pair of sizes we compare the smallest possible sum of a subset of size n
    to the largest sum of a subset of size n - 1. (We increment n until any
    further increase in n would imply that the two subsets would not be
    disjoint. This occurs when n is equal to the integer portion of the length
    of members divided by two.) If the sums of the subsets of size n are
    larger than the sums of the subsets of size n - 1 in every case we know
    that the condition holds and we return True. If any sum of the subset of
    size n - 1 is larger than the associated sum of the subset of size n then
    we have proven that there is at least pair of sizes for which the
    condition does not hold and we return False.

    For example, if members contains 7 elements we compare the sums of these
    pairs of subsets:
        i. The smallest-sum subset of size 2 vs. the largest-sum
            subset of size 1;
        ii. The smallest-sum subset of size 3 vs. the largest-sum
            subset of size 2;
        iii. The smallest-sum subset of size 4 vs. the largest-sum
            subset of size 3.

    :param members:
    :return:
    """
    members_count = len(members)
    sorted_members = sorted(members)  # Sorted to make indexing easier.
    smallest_n_sum = sorted_members[0]  # Smallest sum of an n-member subset.
    largest_n_minus_one_sum = 0  # Largest sum of an (n - 1)-member subset.

    # Compares all n and n - 1 disjoint subset size pairs:
    for index in range(members_count // 2):
        # Adds next-largest item to smallest_n_sum:
        smallest_n_sum += sorted_members[index + 1]

        # Adds next-smallest item to largest_n_minus_one_sum:
        largest_n_minus_one_sum += sorted_members[members_count - index - 1]

        # Condition fails if any smaller subset doesn't have a smaller sum:
        if smallest_n_sum <= largest_n_minus_one_sum:
            return False

    # Returns True if both conditions hold:
    return True


def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise Exception("len(v1) != len(v2)")
    s = 0
    for n in range(len(v1)):
        s += v1[n] * v2[n]
    return s


def cross_product(u, v):
    """

    :param u: [u0, u1]
    :param v: [v0, v1]
    :return: u X v
    """
    return u[0] * v[1] - u[1] * v[0]


class Polynomial:
    def __init__(self, degree=None, coefficients=None):
        if not degree and not coefficients:
            self.degree = 0
            self.coefficients = []
        elif degree and not coefficients:
            self.degree = degree
            self.coefficients = [0] * (degree + 1)
        elif not degree and coefficients:
            self.degree = len(coefficients) - 1
            self.coefficients = coefficients
        elif degree and coefficients:
            if degree != len(coefficients) + 1:
                raise Exception("Degree must be one size greater than the size of coefficients")
            self.degree = degree
            self.coefficients = coefficients

    def get_coefficients(self):
        return self.coefficients

    def get_degree(self):
        return self.degree

    def get_ith_coefficient(self, i):
        return self.coefficients[i]

    def evaluate(self, x):
        result = 0
        for i in range(self.degree + 1):
            result = result * x + self.get_ith_coefficient(i)
        return result


def combinations(n, r):
    c = []  # [0] * nCr(n, r) number of elements of c should be nCr c (n!/(r!(n-r)!)
    a = list(range(r))
    i = 0
    index = r - 1
    while a[0] < n - r + 1:
        while index > 0 and a[index] == n - r + 1:
            index -= 1
        c.append(list(a))
        a[index] += 1
        while index < r - 1:
            a[index + 1] = a[index] + 1
            index += 1
    return c


def is_permutation(n1, n2):
    """
    Return True if n1 is permutation of n2, else false. Assumes n1 and n2 have he same number of digits
    :param n1:
    :param n2:
    :return:
    """
    if n1 == n2:
        return False
    l1 = int(math.log10(n1)) + 1
    l2 = int(math.log10(n2)) + 1
    if l1 != l2:
        return False
    digits = [0] * 10
    for k in range(l1):
        digits[n1 % 10] += 1
        n1 = int(n1 / 10)
        digits[n2 % 10] -= 1
        n2 = int(n2 / 10)
    for d in digits:
        if d != 0:
            return False
    return True


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
    if n == 0 or n == 1:
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
    while n > 0:
        yield a
        a, b, n = b, a + b, n - 1


def tetranacii_sequence(n):
    a, b, c, d = 0, 0, 0, 1
    while n > 0:
        a, b, c, d, n = b, c, d, a + b + c + d, n - 1
        yield d


def sieve_of_eratosthenes(n):
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes  # Algorithm_and_variants
    P = [True for i in range(n+1)]
    P[0] = P[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if P[i]:
            for j in range(i*i, n+1, i):
                P[j] = False
    return P, sorted({k: v for k, v in enumerate(P) if v is True})


def is_prime(n, k=4):
    """
    This has a bug!!
    1 is not a prime
    All primes except 2 are odd
    All primes greater than 3 can be written as 6k+/-1
    Any number n can have only one prime factor greater than sqrt(n)
    :param n: number to test
    :param k: accuracy factor (higher is more accurate), if k = 0, use the original method else use miller rabin
    :return: True or false based on if n is a prime or not
    """
    if n == 1:
        return False
    elif n < 0:
        return False
    elif 1 < n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n == 7: #or n == 9:
        return True
    elif n % 3 == 0:
        return False
    elif n % 5 == 0:
        return False
    else:
        if k == 0:
            r = int(math.floor(math.sqrt(n)))
            d = 5
            while d <= r:
                if n % d == 0:
                    return False
                if n % (d + 2) == 0:
                    return False
                d += 6
        else:
            d = n - 1
            while d % 2 == 0:
                d = d // 2
            for i in range(k):
                if not miller_rabin_test(d, n):
                    return False
    return True


def is_prime1(n):
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


def power(x, y, p):
    """
    Modular exponentiation
    (x ^ y) mod p
    :param x:
    :param y:
    :param p:
    :return: (x ^ y) mod p
    """
    result = 1
    x = x % p
    while y > 0:
        if y & 1:
            result = (result * x) % p
        y = y >> 1
        x = (x * x) % p
    return result


def miller_rabin_test(d, n):
    a = 2 + random.randint(1, n-4)
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d = d * 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def n_primes(n):
    """
    return n primes starting from 2
    :param n: the number of primes to return
    :return: returns a list of primes
    """
    p = [2, 3]
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
    check if a number is palindrome, faster than above
    :param n: the number to be checked
    :return: true or false
    """
    d = int(math.pow(10, int(math.log10(n))))
    while n != 0:
        leading = n // d
        trailing = n % 10
        if leading != trailing:
            return False
        n = (n % d) // 10
        d = d // 100
    return True


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
        return gcd_recursive((u - v) >> 1, v)
    return gcd_recursive((v - u) >> 1, u)


def gcd(u, v):
    if u == v:
        return u
    if u == 0:
        return v
    if v == 0:
        return u
    if u > v:
        n = v
        d = u
    else:
        n = u
        d = v
    while d != 0:
        r = d
        d = n % d
        n = r
    return n


def gcd1(u, v):
    if u == 0:
        return v
    if v == 0:
        return u

    while v != 0:
        if u > v:
            u = u - v
        else:
            v = v - u
    return u


def collatz_sequence(n):
    s = [n]
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
    n = [1]
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


def factor(n, sort=True):
    if n == 0:
        return [0], 0
    ff = []
    lim = int(math.sqrt(n)) + 1
    for d in range(1, lim):
        if n % d == 0:
            ff.append(n // d)
            ff.append(d)
    if sort:
        ff.sort()
    return ff, sum(ff)


def prime_factors(n, number_of_factors=False, p=None):
    if n == 0:
        if number_of_factors:
            return {0: 0}, 0
        else:
            return {0: 0}
    if n == 1:
        if number_of_factors:
            return {1: 1}, 1
        else:
            return {1: 1}
    elif n == 2:
        if number_of_factors:
            return {2: 1}, 1
        else:
            return {2: 1}
    elif n == 3:
        if number_of_factors:
            return {3: 1}, 1
        else:
            return {3: 1}
    ff = {}

    if is_prime(n):
        ff[n] = 1
        if number_of_factors:
            return ff, 1
        else:
            return ff

    while n % 2 == 0:
        if 2 not in ff:
            ff[2] = 1
        else:
            ff[2] += 1
        n = n // 2
    if not p:
        pr = primes_to(math.sqrt(n) + 1)
    else:
        pr = [x for x in p if x <= math.sqrt(n) + 1 ]
    for prms in pr[1::]:
        while n % prms == 0:
            if prms not in ff:
                ff[prms] = 1
            else:
                ff[prms] += 1
            n = n // prms
    if n != 1:
        ff[n] = 1
    if not number_of_factors:
        return ff
    else:
        ps = 1
        for k in ff.keys():
            ps *= ff[k] + 1
        return ff, ps


def is_pandigital(n):
    l = int(math.log(n, 10) + 1)
    s = [False] * 10
    if l > 9:
        return False
    for i in range(l):
        digit = n % 10
        n = int(n / 10)
        if not s[digit]:
            s[digit] = True
        else:
            return False
    if False in s[1:]:
        return False
    else:
        return True


def is_09_pandigital(n):
    l = int(math.log(n, 10) + 1)
    s = [False] * 10
    if l > 10:
        return False
    for i in range(l):
        digit = n % 10
        n = int(n / 10)
        if not s[digit]:
            s[digit] = True
        else:
            return False
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


def get_digits(n, rvrsd=True):
    """
    :param n: number 
    :return: returns the digits in number in revered order
    """
    if n == 0:
        return [0]
    if n < 0:
        n *= -1
    s = []
    l = int(math.log10(n) + 1)
    for i in range(l):
        s.append(n % 10)
        n = n // 10
    if rvrsd:
        return s
    else:
        return s[::-1]


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


def nCr_iterative(n, k):
    """
    Not tested
    :param n:
    :param k:
    :return:
    """
    c = 1
    if k > n - k:
        k = n - k
    for i in range(1, k + 1):
        c = c / i * n % i * n / i
    return c


def nCr(n, r):
    """
    Combinations of n things taken r at a time
    :param n:
    :param r:
    :return:
    """
    if r < 0 or r > n:
        return 0
    if r > n - r:
        r = n - r
    if r == 0 or n <= 1:
        return 1
    return nCr(n - 1, r) + nCr(n - 1, r - 1)


def binomial_coefficient(n, k):
    return nCr(n, k)


def nPr(n, r):
    """
    Permutations of n things r at a time
    :param n:
    :param r:
    :return:
    """
    if r > n:
        return 0
    else:
        return math.factorial(n) // math.factorial(n - r)


def partition_count(m, last=False):
    """
    :param m: number for which to find partition count
    :return: an array with partition counts of all numbers up to m. If last is True will return the
    partition count only for m.
    """
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
    if last:
        return p[m - 1]
    else:
        return p


def partition_array(a):
    """
    Partitions an array a and returns all combinations of partitions
    :param a: an array
    :return:
    """
    if len(a) == 1:
        yield [a]
        return
    first = a[0]
    for s in partition_array(a[1:]):
        for n, sub_set in enumerate(s):
            yield s[:n] + [[first] + sub_set] + s[n + 1:]
        yield [[first]] + s


def unique_partitions(n):
    p = [[n]]
    row = 0
    k = 0
    #p[row].append(n)
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
        n = int(n / 10)
    return s


def convert_array_to_number(a):
    l = len(a)
    if l <= 0:
        return 0
    s = 0
    for n in a:
        s = 10 * s + n
    return s


def primes_to(n):
    """
    return primes starting from 2 less than or equal to n
    :param n: limit
    :return: returns a list of primes
    """
    if n <= 1:
        return 0
    p = [2]
    if n == 2:
        return p
    p.append(3)
    if n == 3:
        return p
    m = p[-1]
    while True:
        m += 2
        if m > n:
            break
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


def phi(n, p=None):
    """
    Returns Eulers Totient function (This function has a bug)
    :param n: number to calculate the totient for
    :param p: a prime array up to square root of n, if not provided will create one
    :return: the totient function
    """
    if n > 10:
        limit = int(math.sqrt(n))
    else:
        limit = n
    if not p:
        p = primes_to(limit)
    i = 0
    _phi = 1
    E = False
    while not E:
        if n % p[i] == 0:
            _phi *= (1 - 1 / p[i])
            temp = n * _phi
        if p[i] >= n or len(p) - 1 == i:
            E = True
        i += 1
    return int(n * _phi)


def phi1(n, p=None):
    """
    Returns Eulers Totient function, faster implementation than phi(n, p)
    :param n: number to calculate the totient for
    :param p: a prime array up to square root of n, if not provided will create one
    :return: the totient function
    """
    if n == 1:
        return 1
    if n < 10:
        limit = n
    else:
        limit = int(math.sqrt(n)) + 1
    if p is None:
        p = prime_factors(limit)
    _phi = n
    i = 0
    if type(p) is dict:
        p = list(p.keys())
    pr = p[i]
    while i < len(p) - 1 and pr * pr <= n:
        if n % pr == 0:
            _phi = _phi - _phi / pr
            while n % pr == 0:
                n = n / pr
        i += 1
        pr = p[i]
    if n > 1:
        _phi = _phi - _phi / n
    return _phi


def phi2(N):
    """
    Returns an array with all totient numbers to N
    :param N:  number to which to calculate phi
    :return: array with totients
    """
    _phi = [0] * (N + 1)
    for n in range(N + 1):
        _phi[n] = n
    for n in range(2, N + 1):
        if _phi[n] == n:
            for m in range(n, N + 1, n):
                _phi[m] = _phi[m] - _phi[m] / n
    return _phi


def is_square(n):
    a = round(math.sqrt(n))
    return a * a == n


def n_phi(n):
    """
    returns a ratio of n to phi(n)
    :param n: number n
    :param p: number of primes to square root on n, calculates if not provided
    :return:
    """
    p = prime_factors(n)
    print(p)
    _n_phi = 1
    for prime_factor in p:
        _n_phi *= prime_factor / (prime_factor - 1)
    return _n_phi


def count(s, n, m):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0 and n >= 1:
        return 1
    return count(s, n, m - 1) + count(s, n - s[m], m)


def roman_2_number(roman):
    number = 0
    last = 0
    subtract = False
    roman = roman[::-1]
    for x in roman:
        current = 0
        if x == "M":
            current = 1000
        elif x == "D":
            current = 500
        elif x == "C":
            current = 100
        elif x == "L":
            current = 50
        elif x == "X":
            current = 10
        elif x == "V":
            current = 5
        elif x == "I":
            current = 1
        if current < last:
            subtract = True
            last = current
        elif current > last:
            subtract = False
            last = current

        if subtract:
            number -= current
        else:
            number += current
    return number


def number_2_roman(number):
    rules = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX",
             5: "V", 4: "IV", 1: "I"}
    roman = ""
    for i in range(len(rules)):
        while number >= list(rules.keys())[i]:
            number -= list(rules.keys())[i]
            roman += rules[list(rules.keys())[i]]
    return roman


def sum_of_proper_factors_excluding_n(n):
    if n == 1:
        return 1
    return sum_of_proper_factors(n) - n


def sum_of_proper_factors(n):
    s = 1
    p = 2
    count = 0
    if n == 1:
        return 1
    while p * p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n = n // p
            while n % p == 0:
                j = j * p
                n = n // p
            s = s * (j - 1)
            s = s // (p - 1)
        if p == 2:
            p = 3
        else:
            p += 2
    if n > 1:
        s = s * (n + 1)
    return s


def create_palindrome(n, odd):
    p = n
    if odd:
        n = n // 10
    while n > 0:
        p = p * 10 + n % 10
        n = n // 10
    return p


def rad(n, p):
    r = 1
    for i in range(len(p)):
        if p[i] > n:
            break
        else:
            if n % p[i] == 0:
                r *= p[i]
    return r


def generate_palindromes(n):
    for j in range(2):
        i = 1
        while create_palindrome(i, j % 2) < n:
            yield create_palindrome(i, j % 2)
            i += 1


def A(n):
    if gcd1(n, 10) != 1:
        return 0
    x = k = 1
    while x != 0:
        x = (x * 10 + 1) % n
        k += 1
    return k


def repunit(n, b=10):
    """

    :param b: base default is 10
    :param n: number of repunits
    :return: number repunit
    """
    assert b >= 2, "b has to be greater than 2"
    assert n >= 1, "n has to be equal to at least 1"
    R = (pow(b, n) - 1) // (b - 1)
    return int(R)


def tens(n):
    result = 1
    while result <= n:
        result *= 10
    return result


# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph

from collections import defaultdict


# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

        # A utility function to find set of an element i

    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

        # A function that does union of two sets of x and y

    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

            # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's
    # algorithm
    def KruskalMST(self):

        result = []  # This will store the resultant MST

        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        # Step 1:  Sort all the edges in non-decreasing
        # order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = [];
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

            # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't cause cycle,
            # include it in result and increment the index
            # of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                # Else discard the edge

        # print the contents of result[] to display the built MST
        print
        total_weight = 0
        "Following are the edges in the constructed MST"
        for u, v, weight in result:
            # print str(u) + " -- " + str(v) + " == " + str(weight)
            print("%d -- %d == %d" % (u, v, weight))
            total_weight += weight
        return result, total_weight


def digit_by_digit_sqrt(number, decimal_places=5):
    # Step 1: Prepare the number by grouping into pairs (e.g., 123 -> '01', '23')
    num_str = str(number)
    if '.' in num_str:
        integer_part, fractional_part = num_str.split('.')
    else:
        integer_part, fractional_part = num_str, ""

    # Ensure even number of digits in the integer part
    if len(integer_part) % 2 != 0:
        integer_part = '0' + integer_part

    # Create groups of pairs
    groups = [int(integer_part[i:i + 2]) for i in range(0, len(integer_part), 2)]

    # Append fractional zeros for requested precision
    # Each pair of zeros after the decimal provides 1 decimal place in the root
    fractional_groups = []
    if fractional_part:
        if len(fractional_part) % 2 != 0: fractional_part += '0'
        fractional_groups = [int(fractional_part[i:i + 2]) for i in range(0, len(fractional_part), 2)]

    groups.extend(fractional_groups)
    while len(groups) < (len(integer_part) // 2 + decimal_places):
        groups.append(0)

    # Core Algorithm
    root = 0
    remainder = 0
    result_digits = []

    #print(f"Step-by-step Calculation for sqrt({number}):\n")

    for i, group in enumerate(groups):
        # Bring down the next group
        current_val = remainder * 100 + group

        # Find the largest digit x such that (20 * root + x) * x <= current_val
        p = root
        x = 0
        for candidate_x in range(1, 10):
            if (20 * p + candidate_x) * candidate_x <= current_val:
                x = candidate_x
            else:
                break

        # Calculate subtraction and update root
        y = (20 * p + x) * x
        remainder = current_val - y
        root = root * 10 + x
        result_digits.append(str(x))

        # Display Step
        step_label = f"Group {i + 1} ({group:02d})"
        #print(f"{step_label:>15}: Current Val: {current_val:<8} | Tried x={x} -> {y} | Remainder: {remainder}")

    # Format output with decimal point
    int_len = len(integer_part) // 2
    final_root = "".join(result_digits[:int_len]) + "." + "".join(result_digits[int_len:])
    return final_root



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
    print("{}".format(get_digits(1)))
    print("{}".format(get_digits(10)))
    print("{}".format(get_digits(2)))
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
    print(primes_to(100))
    print(len(primes_to(100)))
    print(phi(2))
    p = primes_to(100)
    for i in range(2, 11):
        print(i, phi1(i), phi1(i, p), phi(i, p))
    for i in range(2, 11):
        print(i, n_phi(i), n_phi(i))
    p = primes_to(int(math.sqrt(87109)))
    print(phi1(87109))
    #print(prime_factors(87109, p))
    print(phi2(10))
    print(prime_factors(8))
    print(roman_2_number("IX"))
    print(roman_2_number("XI"))
    print(number_2_roman(9))
    print(number_2_roman(11))
    print(combinations(4, 2))
    print(sum_of_proper_factors(220))
    print(sum_of_proper_factors_excluding_n(220))
    print("hello")
    for i in range(101):
        if is_prime(i):
            print("{} is prime".format(i))
    print(partition_count(7))
    print(partition_count(7, True))
    [print(i, end=" ") for i in tetranacii_sequence(0)]
    [print(i, end=" ") for i in tetranacii_sequence(4)]
    print()
    [print(i, end=" ") for i in tetranacii_sequence(7)]
    print()
    [print(i, end=" ") for i in tetranacii_sequence(50)]
    a = [0, 1, 2, 3]
    for p in partition_array(a):
        print(p)
        for n in p:
            print(convert_array_to_number(list(n)))
    print("A(7) = {}".format(A(7)))
    print("A(41) = {}".format(A(41)))
    print("repunit 2 = {}".format(repunit(n=2)))
    print("repunit 3 = {}".format(repunit(n=3)))
    #print("repunit 1000000 = {}".format(repunit(n=1000000)))
    print(tens(456))
    print(f"is 4 a perfect square? {is_square(4)}")
    print(digit_by_digit_sqrt(2, 50))
