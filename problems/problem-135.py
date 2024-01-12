import time

'''

(y + 2d)^2 - (y + d)^2 - y^2 = n
y^2 + 4yd + 4d^2 - y^2 - 2yd - d^2 - y^2 = n
3d^2 + 2yd - y^2 = n

iterate through to the max number, collect number of possible
values in array, by index.

'''

if __name__ == "__main__":
    start = time.time()

    # limit = 100
    limit = 1000000
    solutions = [0] * limit
    S = 0
    n = 0

    for y in range(1, limit):
        for d in range(y // 3 + 1, limit):
            n = 3 * d * d + 2 * y * d - y * y
            print(n)
            if n < 0 or n >= limit:
                break
            else:
                solutions[int(n)] += 1
    #print(solutions)
    for i in solutions:
        if i == 10:
            S += 1
    print(S)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
