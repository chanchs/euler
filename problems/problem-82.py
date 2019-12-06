
import time

if __name__ == "__main__":
    start = time.time()
    l = []
    M = 80

    with open("problem-82.txt") as f:
        for line in f:
            a = list(line.split(','))
            n = [int(x) for x in a]
            l.append(n)

    #M = 5
    #l = [[131, 673, 234,103, 18],
    #    [201, 96, 342,965, 150],
    #    [630, 803, 746,422, 111],
    #    [537,699, 497,121, 956],
    #    [805,732, 524,37, 331]]

    for row in range(M - 1, -1, -1):
        for col in range(M):
            print(" {} ".format(l[row][col]), end="")
        print()

    cost = [l[i][-1] for i in range(M)]
    print("cost = {}".format(cost))
    for r in range(M - 2, -1, -1):
        cost[0] += l[0][r]
        for c in range(1, M):
            cost[c] = min(cost[c], cost[c - 1]) + l[c][r]
        for c in range(M - 2, -1, -1):
            cost[c] = min(cost[c], cost[c + 1] + l[c][r])

    print(min(cost))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
