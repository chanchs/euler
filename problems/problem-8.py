import time

if __name__ == "__main__":
    start = time.time()
    with open("problem-9.txt") as f:
        content = f.read()
    print(content)
    a = list(content)
    print(a)
    n = [int(x) for x in a if x != '\n']
    print(n)

    big = 0
    big_m0 = 0
    big_m1 = 0
    big_m2 = 0
    big_m3 = 0
    big_m4 = 0
    big_m5 = 0
    big_m6 = 0
    big_m7 = 0
    big_m8 = 0
    big_m9 = 0
    big_m10 = 0
    big_m11 = 0
    big_m12 = 0

    for i in range(0, len(n)-12):
        m0 = n[i]
        m1 = n[i + 1]
        m2 = n[i + 2]
        m3 = n[i + 3]
        m4 = n[i + 4]
        m5 = n[i + 5]
        m6 = n[i + 6]
        m7 = n[i + 7]
        m8 = n[i + 8]
        m9 = n[i + 9]
        m10 = n[i + 10]
        m11 = n[i + 11]
        m12 = n[i + 12]

        product = m0 * m1 * m2 * m3 * m4 * m5 * m6 * m7 * m8 * m9 * m10 * m11 * m12
        if product > big:
            big = product
            big_m0 = m0
            big_m1 = m1
            big_m2 = m2
            big_m3 = m3
            big_m4 = m4
            big_m5 = m5
            big_m6 = m6
            big_m7 = m7
            big_m8 = m8
            big_m9 = m9
            big_m10 = m10
            big_m11 = m11
            big_m12 = m12

    print("{0} x {1} x {2} x {3} x {4} x {5} x {6} x {7} x {8} x {9} x {10} x {11} x {12} = {13}".format(big_m0, big_m1,
                                    big_m2, big_m3, big_m4, big_m5, big_m6, big_m7, big_m8, big_m9, big_m10,
                                    big_m11, big_m12, big))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
