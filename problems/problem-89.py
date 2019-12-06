import lib.utilities as ut
import math
import time


if __name__ == "__main__":
    start = time.time()

    saved = 0
    with open("problem-89.txt") as f:
        for roman in f:
            #print("++++++++++++++++++++++")
            print("file :: {}".format(roman), end="")
            number = ut.roman_2_number(roman)
            print("Decimal :: {}".format(number))
            optimized = ut.number_2_roman(number)
            print("Optimized :: {}".format(optimized))
            print("roman = {}, optimized = {}".format(len(roman), len(optimized)))
            saved += len(roman) - len(optimized) - 1  # somehow python is counting the \n as one extra character
            print("cumulative saved = {}".format(saved))
    print("cumulative saved = {}".format(saved - 1))  # except for the last number in the file, which does not have a \n
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

