import time

if __name__=="__main__":
    start = time.time()

    f = open("problem-13.txt")
    s = 0
    for line in f:
        s += int(line)
    print(s)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))