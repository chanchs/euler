import lib.utilities as ut
import time

"""
repunit = (10^N - 1) / 9
e.g. 10 ^ 1 - 1 / 9 = 9 / 9 = 1
     10 ^ 2 - 1 / 9 = 99 / 9 = 11
     10 ^ 3 - 1 / 9 = 999 / 9 = 111
     ...

     if p is prime factor of  the repunit,

     ((10^N - 1) / 9) % p = 0
     or, (10^N - 1) % 9 * p = 0
     or, 10^N % 9p = 1


"""

if __name__ == "__main__":
    start = time.time()

    p = ut.primes_to(100000)

    # k = 2
    # n = ut.repunit(2)

    # print(max(p))
    # Largest = max(p) * max(p)
    # print(Largest)

    # while n < Largest:
    #    n = ut.repunit(k)
    #    if n not in p:
    #        print(n)
            
    #    k += 1
    # k = int(math.pow(10, 9))

    # count = 0
    # i = 0
    # r = 0
    # while count < 40:
    #    if pow(10, k, 9 * p[i]) == 1:
    #        count += 1
    #        r += p[i]
    #        print(p[i])
    #    i += 1

    # print(count)
    # print(r)

    q = pow(10, 20)
    print(q)
    s = 2 + 3

    for pr in p[2:]:
        if pow(10, q, pr) != 1:
            s += pr

    print(s)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
