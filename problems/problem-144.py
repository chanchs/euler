import lib.utilities as ut
import math
import time

def line_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def tangent_slope(x, y):
    return -4 * x / y

def solve_for_x(x1, y1, m):
    n = y1 - m * x1
    a = 4 + m * m
    b = 2 * m * n
    c = n * n - 100
    discriminant = b * b - 4 * a * c
    x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
    if abs(x_1 - x1) > abs(x_2 - x1):
        return x_1
    else:
        return x_2

if __name__ == "__main__":
    start = time.time()
    s = 0
    x0 = 0.0
    y0 = 10.1
    x1 = 1.4
    y1 = -9.6

    while True:
        m1 = line_slope(x0, y0, x1, y1)
        mT = tangent_slope(x1, y1)

        # angle of incidence
        Ai = (m1 - mT) / (1 + m1 * mT)

         # angle of reflection
        Ar = Ai

         # slope of normal
        mN = -1 / mT

        # slope of reflected line
        m2 = (mN - Ar) / (1 + Ar * mN)

        x0 = x1
        y0 = y1

        x1 = solve_for_x(x0, y0, m2)
        y1 = m2 * x1 + (y0 - m2 * x0)

        print(f"{x1}, {y1}")

        s += 1

        if -0.01 < x1 < 0.01 and y1 > 0:
            break

    print(f"Exit Point: {x1}, {y1}")
    print(f"Count = {s}")

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

