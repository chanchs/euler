import time
import lib.utilities as ut

if __name__=="__main__":
    """
    GIven that,
    T = n(n + 1)/2
    P = n(3n -1)/2
    H = n(2n-1)
    
    This solution works because if we set n = 2m -1 for T, we get
    T = n(n + 1)/2 = (2m - 1)(2m - 1 + 1)/2 = 2m(2m - 1)/2 = m(2m - 1) = H
    which leads us to conclude that H is a subset of T when n is odd (2m -1, is always odd). 
    It is then sufficient to generate H (which is already T) and check if it is P, based on the method created for
    problem-44. Start from i = 143 because we aready know that 40755 is the first number to meet the criteria for
    H143. Also, since we know that n has to be odd for the number to be H, we check only the odd numbers (increment the
    loop counter by 2)
    """
    start = time.time()
    E = False
    i = 143
    result = 0
    n = 0
    while E is False:
        i += 2
        n = int(i*(2*i - 1))
        if ut.is_pentagonal(n):
            E = True
            break
    print("result = {}".format(n))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
