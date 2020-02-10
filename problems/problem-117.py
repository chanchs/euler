# https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers
# Tetranacci numbers, the next number is sum of previous 4 numbers

# Pulling out hair, another counting problem. Still hate them.

import lib.utilities as ut
import time

if __name__ == "__main__":
    start = time.time()
    n = 50
    [print(i) for i in ut.tetranacii_sequence(n)]
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
