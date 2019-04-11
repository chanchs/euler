import math
import time
import lib.utilities as ut


def xor(a, b):
    if bool(a) == bool(b):
        return False
    else:
        return a or b


def encrypt(message, key):
    encrypted_message = xor(message, key)
    return encrypted_message


if __name__ == "__main__":
    print("Starting....")
    start = time.time()

    f = open("problem-59.txt")
    encrypted_codes = f.readline().split()
    for encrypted_code in encrypted_codes:
        print(encrypted_code)

    

    f.close()
    end = time.time()
    print("Ending......")
    print("Completed in {0:.2}s".format(end - start))