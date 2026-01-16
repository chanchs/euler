
import lib.utilities as ut
import math
import time



if __name__ == "__main__":
    start = time.time()

    '''
    a * a = x + y
    b * b = x - y
    c * c = x + z => z = c * c - x
    d * d = x - z
    e * e = y + z
    f * f = y - z
    
    2x = x + y + x - y
    2x = a * a + b * b
    
    x = (a * a + b * b) / 2
    y = a * a - x
    z = c * c - x  
    
    Assumption a, b have the same parity and c * c > x 
    '''

    limit = 1000

    for b in range(1, limit):
        for a in range(b + 2, limit, 2):
            x = (a * a + b * b) // 2
            y = a * a - x
            if x > y:
                for c in range(int(math.sqrt(x)), a):
                    z = c * c - x
                    if z < y :
                        if ut.is_square(x - z) and ut.is_square(y + z) and ut.is_square(y - z):
                            print(x + y + z)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

