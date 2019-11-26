
import time

# http://mathworld.wolfram.com/PartitionFunctionP.html

if __name__ == "__main__":
    start = time.time()

    mx = 1000000
    p = [1] * mx
    for i in range(1, mx):
        j = k = 1
        s = 0
        while j > 0:
            j = int(i - (3 * k * k + k) / 2)
            if j >= 0:
                if k & 1:
                    s += p[j]
                else:
                    s -= p[j]
            j = int(i - (3 * k * k - k) / 2)
            if j >= 0:
                if k & 1:
                    s += p[j]
                else:
                    s -= p[j]
            s %= mx
            k += 1
        p[i] = s
        if s == 0:
            print(i)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
