import itertools
import time


def check_result(p):
    if (p[1] == 10 or
            p[2] == 10 or
            p[4] == 10 or
            p[6] == 10 or
            p[8] == 10):
        return False
    if (p[0] > p[3] or
            p[0] > p[5] or
            p[0] > p[7] or
            p[0] > p[9]):
        return False
    if p[0] + p[1] + p[2] != p[3] + p[2] + p[4]:
        return False
    if p[0] + p[1] + p[2] != p[5] + p[4] + p[6]:
        return False
    if p[0] + p[1] + p[2] != p[7] + p[6] + p[8]:
        return False
    if p[0] + p[1] + p[2] != p[9] + p[8] + p[1]:
        return False
    return True


if __name__ == "__main__":
    print("Starting....")
    start = time.time()
    v = []
    n = ""
    for i in range(1, 11):
        v.append(i)
    for p in itertools.permutations(v, 10):
        if check_result(p):
            s = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(p[0], p[1], p[2], p[3], p[2], p[4], p[5], p[4], p[6], p[7],
                  p[6], p[8], p[9], p[8], p[1])
            if s > n:
                n = s
    print("{}".format(s))

    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))
