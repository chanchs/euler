import time
import math
import lib.utilities as ut


def is_concatenated_prime(n1, n2):
    l1 = int(math.log10(n1) + 1)
    l2 = int(math.log10(n2) + 1)
    num1 = int(math.pow(10, l1) * n2 + n1)
    num2 = int(math.pow(10, l2) * n1 + n2)
    if ut.is_prime(num1) and ut.is_prime(num2):
        return True
    else:
        return False


def calculate():
    P = ut.n_primes(10000)
    print(P)
    p1 = p2 = p3 = p4 = p5 = 0
    l = len(P)
    for i in range(l):
        p1 = P[i]
        for j in range(l):
            p2 = P[j]
            if p2 <= p1:
                if is_concatenated_prime(p1, p2):
                    print("p1 = {}, p2 = {}".format(p1, p2))
                    for k in range(l):
                        p3 = P[k]
                        if p3 <= p2:
                            if is_concatenated_prime(p2, p3) and is_concatenated_prime(p1, p3):
                                print("p1 = {}, p2 = {}, p3 = {}".format(p1, p2, p3))
                                for m in range(l):
                                    p4 = P[m]
                                    if p4 <= p3:
                                        if is_concatenated_prime(p4, p3) and is_concatenated_prime(p4, p2) \
                                                and is_concatenated_prime(p4, p1):
                                            print("p1 = {}, p2 = {}, p3 = {}, p4 = {}".format(p1, p2, p3, p4))
                                            for n in range(l):
                                                p5 = P[n]
                                                if p5 <= p4:
                                                    if is_concatenated_prime(p5, p4) and is_concatenated_prime(p5, p3) \
                                                            and is_concatenated_prime(p5, p2) \
                                                            and is_concatenated_prime(p5, p1):
                                                        print("p1 = {}, p2 = {}, p3 = {}, p4 = {}, "
                                                              "p5 = {}".format(p1, p2, p3, p4, p5))
                                                        print(p1 + p2 + p3 + p4 + p5)
                                                        return


if __name__ == "__main__":
    print("Starting....")
    start = time.time()
    calculate()
    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))
