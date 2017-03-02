import time

if __name__=="__main__":
    start = time.time()
    line_number = 0
    with open("problem-22.txt") as f:
        content = f.read()
    content = content.replace('"', '')
    names = content.split(",")
    ts = 0
    names.sort()
    for name in names:
        s = 0
        line_number += 1
        n = [ord(a) - 64 for a in name]
        s = sum(n)
        ts += s * line_number
        print("{0}, {1}, {2}, {3}, {4}".format(line_number, name, n, s, ts))
    print("total score = {0}, line_number = {1}".format(ts, line_number))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))