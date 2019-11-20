import math
import time

from lib.utilities import get_digits

if __name__ == "__main__":
    print("Starting....")
    start = time.time()
    f = [0] * 10
    for n in range(10):
        f[n] = math.factorial(n)
    print(f)
    N = 1000000
    count = 0
    number_sums = {}
    while n > 1:
        n = N
        chain = {}
        E = True
        while E:
            s = 0
            if n in number_sums:
                s = number_sums[n]
            else:
                digits = get_digits(n)
                for d in digits:
                    s += f[d]
                number_sums[n] = s
            if n not in chain:
                chain[n] = s
                n = s
            else:
                E = False
                N -= 1
        print("for {} length of chain is {}".format(N + 1, len(chain)))
        if len(chain) == 60:
            count += 1
    print(count)
    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))
