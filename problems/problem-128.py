import lib.utilities as ut
import time


if __name__ == "__main__":
    start = time.time()

    count = 1
    limit = 2000
    n = number = 0

    while count < limit:
        n += 1
        if ut.is_prime1(6 * n - 1) and ut.is_prime1(6 * n + 1) and ut.is_prime1(12 * n + 5):
            count += 1
            number = 3 * n * n - 3 * n + 2
            if count > limit:
                break
        if ut.is_prime1(6 * n + 5) and ut.is_prime1(6 * n - 1) and ut.is_prime1(12 * n - 7) and n != 1:
            count += 1
            number = 3 * n * n + 3 * n + 1
    print(number)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
