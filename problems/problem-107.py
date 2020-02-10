# https://en.wikipedia.org/wiki/Kruskal%27s_algorithm, implementation of the algorithm from
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
# and some minor modifications
import math
import time
import lib.utilities as ut


if __name__ == "__main__":
    start = time.time()

    initial_sum = 0
    nodes = set()
    network = []

    s = []
    with open("problem-107.txt") as f:
        for line in f:
            line = line.replace("-", "0", 41)
            s.append([int(x) for x in list(line.strip().split(","))])

    g = ut.Graph(40)
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i][j] != 0 and i < j:
                #initial_sum, network, nodes = add_edge(i, j, s[i][j], initial_sum, network, nodes)
                initial_sum += s[i][j]
                g.addEdge(i, j, s[i][j])
                print(i, j, s[i][j])

    # Driver code
    #g = Graph(4)
    #g.addEdge(0, 1, 10)
    #g.addEdge(0, 2, 6)
    #g.addEdge(0, 3, 5)
    #g.addEdge(1, 3, 15)
    #g.addEdge(2, 3, 4)

    result, final_sum = g.KruskalMST()
    print(result)
    print("Initial sum = {}, optimized sum, = {} saving = {}".format(initial_sum, final_sum, initial_sum - final_sum))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
