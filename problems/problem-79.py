import lib.utilities as ut
import time


def swap(i, j, n):
    temp = n[i]
    n[i] = n[j]
    n[j] = temp
    return n


if __name__ == "__main__":
    start = time.time()

    attempts = []
    key = []

    with open("problem-79.txt") as input_file:
        for line in input_file:
            row = int(line)
            attempts.append(row)
            n = ut.get_digits(row, False)
            ######################
            if n[0] not in key:
                key.append(n[0])
            if n[1] not in key:
                key.append(n[1])
            if n[2] not in key:
                key.append(n[2])
            ###################
            # code block above can be done as key = list(set(key)) outside the loop
    print(attempts)
    print(key)
    for attempt in attempts:
        a = ut.get_digits(attempt, False)
        first = a[0]
        second = a[1]
        third = a[2]

        f_index = key.index(first)
        s_index = key.index(second)
        if f_index > s_index:
            key = swap(f_index, s_index, key)
        s_index = key.index(second)
        t_index = key.index(third)
        if s_index > t_index:
            key = swap(s_index, t_index, key)
    print("key = {}".format(key))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
