from operator import add, sub, mul, truediv
from itertools import combinations, permutations, product
import time


def seq_length(s, c=1):
    while c in s:
        c += 1
    return c - 1


if __name__ == "__main__":
    start = time.time()

    max_t = max_s = 0
    for terms in combinations(range(1, 10), 4):
        print(terms)
        s = set()
        for n in permutations(terms):
            print(n)
            for op in product([add, sub, mul, truediv], repeat=3):
                x = op[0](op[1](n[0], n[1]), op[2](n[2], n[3]))  # (a.b) (c.d)
                if x % 1 == 0 and x > 0:
                    s.add(int(x))
                x = op[0](op[1](op[2](n[0], n[1]), n[2]), n[3])  # (((a.b).c).d)
                if x % 1 == 0 and x > 0:
                    s.add(int(x))
            if seq_length(s) > max_s:
                max_s = seq_length(s)
                max_t = terms
    print("".join(str(i) for i in max_t))


    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
