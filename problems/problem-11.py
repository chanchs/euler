import time

if __name__=="__main__":
    start = time.time()

    l = []
    f = open("problem-11.txt")

    for line in f:
        a = list(line.split())
        #print(a)
        n = [int(x) for x in a]
        l.append(n)

    #print(l)
    r = len(l)
    c = len(l[0])

    print("r = {}".format(r))
    print("c = {}".format(c))

    s = []
    for i in range(r - 3):
        for j in range(c - 3):
            s.append(l[i][j] * l[i][j + 1] * l[i][j + 2] * l[i][j + 3])
            s.append(l[i][j] * l[i + 1][j + 1] * l[i + 2][j + 2] * l[i + 3][j + 3])
            s.append(l[i + 3][j] * l[i + 2][j + 1] * l[i + 1][j + 2] * l[i][j + 3])
            s.append(l[i][j] * l[i + 1][j] * l[i + 2][j] * l[i + 3][j])

    s.sort()
    print(s[len(s) - 1])
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))