# Reference https://books.google.com/books?id=D_XmfolL-IUC&printsec=frontcover&dq=isbn:0817645497&hl=en&newbks=1&newbks_redir=0&sa=X&ved=2ahUKEwiY9anO7MLmAhWPTt8KHeKgBOQQ6AEwAHoECAAQAg#v=onepage&q&f=false


"""
Completed this in excel and the pinched the program from one of the solutions in the Forum.
		2a	2a+1
2	3	6	7
3	3	6	7
5	2	4	5
7	2	4	5
11	1	2	3
13	1	2	3
17	1	2	3
19	1	2	3
23	1	2	3
29	1	2	3
31	1	2	3
37	1	2	3
	18	pi(2a + 1)	 8,037,225.00
		pi(2a + 1)/2	 4,018,612.50


			N
			9.35013E+15
"""

import functools
import time


def odd_factors(n):
    f = []
    i = 3
    while i*i <= n:
        while not (n % i):
            f.append(i)
            n = n / i
        i += 2
    if n > 1:
        f.append(n)
    return f


if __name__ == "__main__":
    start = time.time()
    N = 8 * (10 ** 6)

    while True:
        N += 1
        f = odd_factors(N)
        if max(f) > 7:
            continue
        break
    f.reverse()
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    v = functools.reduce(lambda x, y: x*y, [primes[i]**((p-1)/2) for i, p in enumerate(f)])
    print(v)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))