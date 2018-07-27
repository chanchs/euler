import math
import time
import lib.utilities as ut


def generate_triangle_numbers(n):
    tn = [0] * (n + 1)
    for i in range(n + 1):
        tn[i] = int(0.5 * i * (i + 1))
    return tn


def calculate_weight(word):
    alphabet = {'A': 1,
                'B': 2,
                'C': 3,
                'D': 4,
                'E': 5,
                'F': 6,
                'G': 7,
                'H': 8,
                'I': 9,
                'J': 10,
                'K': 11,
                'L': 12,
                'M': 13,
                'N': 14,
                'O': 15,
                'P': 16,
                'Q': 17,
                'R': 18,
                'S': 19,
                'T': 20,
                'U': 21,
                'V': 22,
                'W': 23,
                'X': 24,
                'Y': 25,
                'Z':26}
    weight = 0
    for i in range(len(word)):
        weight += alphabet[word[i]]
    return weight


if __name__=="__main__":
    start = time.time()

    f = open("problem-42.txt")
    words = f.read().replace("\"","").rstrip("\r\n").split(",")

    tn = generate_triangle_numbers(len(words))

    count = 0
    print(tn)
    for word in words:
        w = calculate_weight(word)
        if w in tn:
            count += 1

    print(count)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
