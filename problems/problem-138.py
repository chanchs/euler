import time


def generating_function(x_0, x_1):
    return x_1 * 18 - x_0


if __name__ == "__main__":
    start = time.time()
    l_sum = 0
    l1 = 0
    l2 = 0
    b = 2

    L1 = 0
    L2 = 0
    count = 1

    key = False

    x0 = 1
    x1 = 17
    print(x1)

    while count <= 12:
        x = generating_function(x0, x1)
        print(f"{x1} * 18 - {x0} = {x}")
        x0 = x1
        x1 = x
        l_sum += x0
        count += 1

    print(l_sum)


    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
