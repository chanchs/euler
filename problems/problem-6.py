import utility as ut
import time

if __name__=="__main__":

    start = time.time()

    sum_of_squares = sum([x*x for x in range(1, 101)])
    intermediate = time.time()
    print("sum of squares = {0} in {1:.2}s".format(sum_of_squares, intermediate - start))
    square_of_sums = sum([x for x in range(1, 101)]) ** 2
    intermediate2 = time.time()
    print("square of sums = {0} in {1:.2}s".format(square_of_sums, intermediate2 - intermediate))

    diff = square_of_sums - sum_of_squares

    print("diff = {}".format(diff))

    end = time.time()

    print("Completed in {0:.2}s".format(end-start))