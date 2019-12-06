import lib.utilities as ut


import time

if __name__ == "__main__":
    start = time.time()
    l = []
    M = 80

    with open("problem-81.txt") as f:
        for line in f:
            a = list(line.split(','))
            # print(a)
            n = [int(x) for x in a]
            l.append(n)

    #M = 5
    #l = [[131, 673, 234,103, 18],
    #    [201, 96, 342,965, 150],
    #    [630, 803, 746,422, 111],
    #    [537,699, 497,121, 956],
    #    [805,732, 524,37, 331]]

    for row in range(M):
        for col in range(M):
            print(" {} ".format(l[row][col]), end="")
        print()

    #row = col = M - 1
    #s = l[row][col]
    #print(l[row][col])
    #print("Initial s = {}".format(s))
    for r in range(M):
        for c in range(M):
            if r * c > 0:
                l[r][c] += min(l[r - 1][c], l[r][c - 1])
            else:
                if r:
                    l[r][c] += l[r - 1][c]
                elif c:
                    l[r][c] += l[r][c - 1]

    print(l[-1][-1])

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
