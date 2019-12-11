import lib.utilities as ut
import time


if __name__ == "__main__":
    start = time.time()

    limit = 10000000
    terminate = {}
    count = 0
    test = [44, 85]
    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # for i in test:
    for i in range(1, limit):
        print(i)
        n = i
        s = 0
        chain = [n]
        while True:
            #print(n)
            d = ut.get_digits(n)
            s = sum(squares[x] for x in d)
            #print(s)
            if s in terminate:
                if terminate[s] == 89:
                    count += 1
                    break
            chain.append(s)
            if s == 1 or s == 89:
                # print("{} :: {}".format(i, s))
                if s == 89:
                    count += 1
                    #print("{} :: {}".format(n, s))
                for k in chain:
                    terminate[k] = s
                break
            else:
                n = s
    print(terminate)
    print("Count = {}".format(count))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
