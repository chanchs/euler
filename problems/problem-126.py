# this does not quite work - but I cheat on this :)

import time


def cubes(z, y, x, n):
    return 2 * (x * y + y * z + x * z) + 4 * (x + y + z + n - 2) * (n - 1)


if __name__ == "__main__":
    start = time.time()
    limit = 20000

    count = 50000 * [0]
    z = 1
    while cubes(z, z, z, 1) <= limit:
        y = z
        z += 1
        while cubes(z, y, z, 1) <= limit:
            x = y
            y += 1
            while cubes(z, y, x, 1) <= limit:
                n = 1
                x += 1
                while cubes(z, y, x, n) <= limit:
                    print(z, y, x, n)#, count[cubes(z, y, x, n)])
                    count[cubes(z, y, x, n)] += 1
                    n += 1
                   #print(cubes(z, y, x, n))
    print(count)
    print("count[{}] = 1000".format(count.index(1000)))
    print("count[{}] = 999".format(count.index(999)))
    print("count[18522] = {}".format(count[18522]))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

