import lib.utilities as ut
import time

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def next_permutation():
    N = len(numbers)
    i = N - 1

    while numbers[i - 1] >= numbers[i]:
        i = i - 1
        if i == 0:
            return False
    j = N
    while numbers[j - 1] <= numbers[i - 1]:
        j = j - 1

    swap(i - 1, j - 1)
    i += 1
    j = N
    while i < j:
        swap(i - 1, j - 1)
        i += 1
        j -= 1
    return True


def swap(i, j):
    k = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = k


def check_partitions(start_index, previous):
    count = 0
    for i in range(start_index, len(numbers)):
        number = 0
        for j in range(start_index, i + 1):
            number = number * 10 + numbers[j]
        if number < previous:
            continue
        if not ut.is_prime1(number):
            continue
        if i == len(numbers) - 1:
            return count + 1
        count += check_partitions(i + 1, number)
    return count


if __name__ == "__main__":
    start = time.time()
    count = 0
    while next_permutation():
        count += check_partitions(0, 0)
    print(count)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
