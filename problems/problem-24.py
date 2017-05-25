import itertools
import time


if __name__=="__main__":
    start = time.time()
    mm = 9
    v = []

    for i in range(0, mm + 1):
        v.append(i)

    count = 0
    for p in itertools.permutations(v, 10):
        print(p)
        count = count + 1
        if count > 999999:
            break

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))