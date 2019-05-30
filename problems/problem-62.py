import time
import lib.utilities as ut

# this works because permutation of a number will still have the same digits, it's enough to verify that the digits
# in the number are the same. The smaller number is retrieved by index function, because it returns the first
# instance of the array that it finds in the list.

def get_sorted_digits(n):
    y = ut.get_digits(n)
    y.sort()
    return y


if __name__ == "__main__":
    print("Starting....")
    start = time.time()
    cubes = []
    i = 1
    while True:
        cube = i ** 3
        s = get_sorted_digits(cube)
        cubes.append(s)
        if cubes.count(s) == 5:
            print((cubes.index(s) + 1) ** 3)  # index starts from 0, and we need the cube
            break
        else:
            i += 1

    end = time.time()
    print("Ending......")
    print("Completed in {:.2}s".format(end - start))
