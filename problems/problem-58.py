import math
import time
import lib.utilities as ut


if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    p, pr = ut.sieve_of_eratosthenes(1000000000)
    #print(p)
    #print(pr)

    index = 3
    gap = 2
    diagonal_number_count = 1 # adjust for the center
    prime_diagonal_count = 0

    while True:
        print(index, p[index])
        c1 = index
        if p[index]:
            prime_diagonal_count += 1
        index += gap
        print(index, p[index])
        c2 = index
        if p[index]:
            prime_diagonal_count += 1
        index += gap
        print(index, p[index])
        c3 = index
        if p[index]:
            prime_diagonal_count += 1
        index += gap
        print(index, p[index])
        c4 = index
        if p[index]:
            prime_diagonal_count += 1

        diagonal_number_count += 4

        ratio = prime_diagonal_count / diagonal_number_count

        print("{0} :: {1} :: {2:.2} :: lenght = {3}".format(diagonal_number_count, prime_diagonal_count, ratio,
                                                            math.ceil(diagonal_number_count/2)))

        gap += 2
        index += gap

        if index >= len(p):
            break
        if ratio < 0.10:
            break


    end = time.time()
    print("Ending......")
    print("Completed in {0:.2}s".format(end - start))