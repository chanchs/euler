import lib.utilities as ut
import time

'''
https://oeis.org/A081018
Fibonacci(2n)*Fibonacci(2n+1)
'''

if __name__ == "__main__":
    start = time.time()

    # limit = 100

    n = 15

    A = ut.n_th_fibonacci(2 * n) * ut.n_th_fibonacci(2 * n + 1)

    print(A)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

