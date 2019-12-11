import lib.utilities as ut
import time


class Triangle:
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.l2 = [(x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1),
                   (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2),
                   (x2 - x0) * (x2 - x0) + (y2 - y0) * (y2 - y0)]
        self.compare_string = "{} {} {} {} {} {}".format(self.x0, self.y0, self.x1, self.y1, self.x2, self.y2)

    def is_right(self):
        if self.l2[0] == 0 or self.l2[1] == 0 or self.l2[2] == 0:
            return False
        elif self.l2[2] == self.l2[1] + self.l2[0]:
            return True
        elif self.l2[1] == self.l2[0] + self.l2[2]:
            return True
        elif self.l2[0] == self.l2[1] + self.l2[2]:
            return True
        return False


if __name__ == "__main__":
    start = time.time()

    limit = 50
    tr = []
    x3 = y3 = 0
    count = 0
    # Px <= Qx and Py >= Qy
    for x1 in range(limit + 1):
        for y2 in range(limit + 1):
            for x2 in range(x1, limit + 1):
                for y1 in range(y2, limit + 1):
                    t = Triangle(x1, y1, x2, y2, x3, y3)
                    if t.is_right():
                        count += 1
                        tr.append(t)
                        print("{} :: {} :: ({}, {}), ({}, {}), ({}, {})".format(count, t.compare_string,
                                                                                x1, y1,
                                                                                x2, y2,
                                                                                x3, y3))

    print("count = {}".format(count))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
