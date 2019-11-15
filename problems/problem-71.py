import time


if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    a = 3
    b = 7
    N = 1000000
    best_num = 0
    best_denom = 1
    curr_denom = N
    min_denom = 1

    while curr_denom >= min_denom:
        curr_num = int((a * curr_denom - 1) / b)
        if best_num * curr_denom < curr_num * best_denom:
            best_num = curr_num
            best_denom = curr_denom
            delta = a * curr_denom - b * curr_num
            min_denom = int(curr_denom / delta + 1)
        curr_denom = curr_denom - 1
    print(best_num, best_denom)

    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))
