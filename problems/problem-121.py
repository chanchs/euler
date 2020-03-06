import time


if __name__ == "__main__":
    start = time.time()

    limit = 15
    outcomes = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

    print(limit, outcomes)

    for i in range(2, limit + 1):
        for j in range(len(outcomes) - 1):
            outcomes[j] = outcomes[j + 1]
        outcomes[limit] = 0

        for j in range(len(outcomes) - 1, 0, -1):
            outcomes[j] += outcomes[j - 1] * i
    positive = 0
    for i in range(int(limit / 2 + 1)):
        positive += outcomes[i]
    total = 1
    for i in range(2, limit + 2):
        total *= i
    print(positive, total, int(total / positive))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

