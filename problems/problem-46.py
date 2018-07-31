import math
import time
import lib.utilities as ut

if __name__ == "__main__":
    start = time.time()
    p = ut.n_primes(800)
    key = False
    index = 0
    n = 9
    while key is not True:
        if n not in p:
            for prime in p:
                if prime < n:
                    s = (n - prime) / 2
                    if math.sqrt(s) == int(math.sqrt(s)):
                        print("{0} = {1} + 2 * {2}^2".format(n, prime, int(math.sqrt(s))))
                        break
                else:
                    key = True
                    print("Conjecture fails for {}".format(n))
                    break
        n += 2
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))