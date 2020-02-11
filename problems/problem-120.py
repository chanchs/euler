import time


if __name__ == "__main__":
    start = time.time()

    r = r_max = 0

    for a in range(3, 1001):
        N = int((a - 1) / 2)
        r = 2 * N * a
        r_max += r
        print(a, r_max)

    print(r_max)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
