import math
import time
import lib.utilities as ut

if __name__=="__main__":
    start = time.time()
    palindrome_sum = 0
    for n in range(1, 1000001, 2):
        b = ut.convert_decimal_to_binary(n)
        if ut.is_palindrome(b) and ut.is_palindrome(n):
            palindrome_sum += n
            print("{0}, {1}, sum = {2}".format(n, b, palindrome_sum))
    print("sum of palindromes = {}".format(palindrome_sum))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
