import time


if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    tr = []
    s = 0
    total_rows = 100

    with open("problem-67.txt") as input_file:
        for line in input_file:
            row = [int(x) for x in line.split()]
            tr.append(row)

    for r in range(total_rows - 2, -1, -1):
        for c in range(r + 1):
            tr[r][c] += max(tr[r + 1][c], tr[r + 1][c + 1])

    print("sum = {}".format(tr[0][0]))
    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))
