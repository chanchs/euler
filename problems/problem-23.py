import time

if __name__=="__main__":
    start = time.time()

    max = 28123
    sum = 0
    n = []
    a = []

    for i in range(1, max + 1):
        sum = 0
        n.append(i)

        j = 1
        for j in range(1, int(i/2) + 1):
            if i % j == 0:
                sum += j

            j = j + 1

        if sum > i:
            #print("{} is abundant".format(i))
            a.append(i)
        #elif sum < i:
        #    print("{} is deficient".format(i))
        #elif sum == i:
        #    print("{} is perfect".format(i))

    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum = a[i] + a[j]

            if sum in n:
                n.remove(sum)
                print("{0} is sum of {1} + {2}".format(sum, a[i], a[j]))
            elif sum > max:
                break

    sum = 0
    for i in range(len(n)):
        sum += n[i]

    print("non abundant sum = {}".format(sum))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))