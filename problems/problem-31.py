import time


def count(s, n, m):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <=0 and n >= 1:
        return 1
    return count(s, n, m - 1) + count(s, n - s[m], m)

if __name__=="__main__":
    start = time.time()
    s = [1, 2, 5, 10, 20, 50, 100, 200]
    ans = count(s, 200, 6) + 1
    print("count = {}".format(ans))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))