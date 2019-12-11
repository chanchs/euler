# stole the solution from https://blog.dreamshire.com/project/source/pe95.py
import lib.utilities as ut
import time


def calculate_amicable_chains(L=1000000):
    d = [1] * L
    for i in range(2, L//2):
        for j in range(2*i, L, i):
            d[j] += i
    min_link = 0
    max_cl = 0
    for i in range(2, L):
        n, chain = i, []
        while d[n] < L:
            d[n], n = L+1, d[n]
            try: k = chain.index(n)
            except ValueError: chain.append(n)
            else:
                if len(chain[k:]) > max_cl:
                    max_cl, min_link = len(chain[k:]), min(chain[k:])
    return min_link


if __name__ == "__main__":
    start = time.time()
    print(calculate_amicable_chains())
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
