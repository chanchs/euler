import time
import lib.utilities as ut

if __name__=="__main__":
    start = time.time()
    p = []
    s = 0
    for a in range(1, 999):
        for b in range(a, 10000):
            pl = a * b
            if pl in p:
                break
            if len(str(pl) + str(a) + str(b)) > 9:
                break
            p_str = str(pl) + str(a) + str(b)
            if ut.is_pandigital(int(p_str)):
                #print("string = {0}, product = {1}, a = {2}, b = {3}".format(p_str, pl, a, b))
                s += pl
                p.append(pl)
    print("sum of products = {}".format(s))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))