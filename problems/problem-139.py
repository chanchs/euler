import lib.utilities as ut
import math
import time

import lib.utilities as ut
import math
import time


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_perfect_square(n):
    sq = math.isqrt(n)
    return True if n == sq * sq else False

def find_triangles(limit):
    count = 0
    mlimit = math.isqrt(limit)
    #mlimit = 2 * limit

    for m in range(3, mlimit, 2):
        for n in range(1, m):
            if (m + n) % 2 == 1 and math.gcd(m, n) == 1:
                a = (m * m - n * n)
                b = 2 * m * n
                c = (m * m + n * n)

                if a < b:
                    a, b = b, a

                if math.gcd(a, b) == 1 and c % (a - b) == 0:
                    p = m * (m + n) * 2
                    count += (limit - 1) // p

    return count

def generate_primitive_pythagorean_triplets(max_limit):
    for m in range(2, int(max_limit**0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                if c > max_limit:
                    break
                yield (a, b, c)


def generate_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit):
        for b in range(a, limit):
            c = int((a*a + b*b)**0.5)
            if c > limit:
                break
            if a*a + b*b == c*c:
                triplets.append((a, b, c))
    return triplets

def fibonacci_pythagorean_triplets(max_limit):
    a, b = 1, 1
    while True:
        c = a + b
        m, n = b, a
        if m > n:
            triplet = (m*m - n*n, 2*m*n, m*m + n*n)
            if max(triplet) > max_limit:
                break
            yield triplet
        a, b = b, c


def find_triangles2(limit):
    count = 0
    mlimit = int((limit / 2) ** 0.5)
    seen = set()

    for m in range(2, mlimit):
        for n in range(1, m):
            if (m + n) % 2 == 1 and ut.gcd(m, n) == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n

                if a + b + c >= limit:
                    break

                # ensure a > b
                if a < b:
                    a, b = b, a

                # key optimization: check if 2ab is a perfect square
                # this is necessary for the tiling to be possible
                area_2ab = 2 * a * b
                sqrt_2ab = int(pow(area_2ab, 0.5))
                if sqrt_2ab * sqrt_2ab != area_2ab:
                    continue

                # key optimization: check primitive triple only once
                if (a, b, c) in seen:
                    continue
                seen.add((a, b, c))

                # find valid multiples
                k = 1
                while k * (a + b + c) < limit:
                    # The condition for tiling is that c²-(a-b)² must be divisible by unit squares
                    # This simplifies to: 2ab must be a perfect square
                    count += 1
                    k += 1

    return count

def find_triangles_3(limit):
    LIMIT = 100000000

    # Pythagorean triples theorem:
    #   Every primitive Pythagorean triple with a odd and b even can be expressed as
    #   a = st, b = (s^2-t^2)/2, c = (s^2+t^2)/2, where s > t > 0 are coprime odd integers.
    ans = 0
    for s in range(3, math.isqrt(LIMIT * 2), 2):
        for t in range(1, s, 2):
            a = s * t
            b = (s * s - t * t) // 2
            c = (s * s + t * t) // 2
            p = a + b + c
            if p >= LIMIT:
                break
            if c % (a - b) == 0 and math.gcd(s, t) == 1:
                ans += (LIMIT - 1) // p
    return str(ans)



if __name__ == "__main__":
    start = time.time()
    print(find_triangles(100000000))
    print(find_triangles_3(1000))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

if __name__ == "__main__1":
    start = time.time()
    key = False

    count = 0

    Plimit = 100000000
    limit = int(math.sqrt(Plimit))

    for triplet in generate_pythagorean_triplets(Plimit):
        print(f"triplet = {triplet}")
        a = triplet[0]
        b = triplet[1]
        c = triplet[2]

        p = a + b + c
        sq = c * c
        tr = int(0.5 * 4 * a * b)
        diff = int(sq - tr)

        if sq % diff == 0 and p <= Plimit:
            print(f"({a}, {b}, {c}), "
                  f"p = {p}, "
                  f"area = {tr / 4}, "
                  f"4 * area = {2 * a * b}, "
                  f"c^2 = {c * c}, "
                  f"{sq} - {tr} = {diff}, "
                  f"{sq} % {diff} = {sq % diff}")
            count += 1

    print(f"Number of triples = {count}")

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

