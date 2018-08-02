import math
import time
from collections import Counter
import lib.utilities as ut

checked = []
primes = []


def replace_repeated_digits(n):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    str_n = str(n)
    repeat = Counter(str_n)
    set_n = Counter(set(str_n))
    sol = []
    #print(repeat - set_n)
    for repeats in (repeat - set_n):
        temp = [int(str_n.replace(repeats, x)) for x in numbers]
        sol.append(temp)
    return sol


def remove_non_primes(numbers):
    for p in numbers:
        checked.append(p)
        if p > 0:
            if ut.is_prime(p) is not True or int(math.log10(p)) + 1 < 5:
                numbers.remove(p)
    return numbers


if __name__ == "__main__":
    print("Starting....")
    start = time.time()
    primes = ut.n_primes(80000)
    #print(primes)
    primes = [x for x in primes if len(str(x)) - len(set(str(x))) >= 3]
    #print(primes)
    E = False
    index = 0
    while not E:
        if primes[index] not in checked:
            #print(primes[index])
            replacements = replace_repeated_digits(primes[index])
            for j in replacements:
                #print(j)
                pp = remove_non_primes(j)
                #print(pp)
                #y = [x for x in pp if int(math.log10(x) + 1) > 4]
                if len(pp) == 8:
                    print(j[0])
                    E = True
                    break
        index += 1
    end = time.time()
    print("Ending......")
    print("Completed in {0:.2}s".format(end - start))