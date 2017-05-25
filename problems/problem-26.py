import time


def divrest(a, b):
    rems = []
    r = 1
    k = 0
    #print("a = {0}, b = {1}".format(a, b))
    while r != 0:
        k = a / b
    #    print("k = {}".format(k))
        if k < 1:
            a = a * 10
            k = a / b
        r = a % b
        if r not in rems:
            rems.append(r)
        else:
           break
        a = r
    #print(rems)
    return len(rems)


if __name__=="__main__":
    start = time.time()

    n = 1000
    mx = 0
    d = 0
    for i in range(1, n):
        kk = divrest(1, i)
        if kk > mx:
            mx = kk
            d = i
    print("Max = {0} for  d = {1}".format(mx, d))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))