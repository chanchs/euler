# http://wiki.san-ss.com.ar/project-euler-problem-109

import math
import time
import lib.utilities as ut


if __name__ == "__main__":
    start = time.time()

    limit = 100

    doubles = set(2 * x for x in range(1, 21))
    doubles.add(50)
    casual = sorted(
        [x for x in range(1, 21)] + [2 * x for x in range(1, 21)] + [3 * x for x in range(1, 21)] + [25] + [50])
    result = 0
    for score in range(2, limit):
        if score in doubles:
            result += 1
        for first in casual:
            if first >= score:
                break
            result += (score - first) in doubles and 1 or 0
        first = 0
        while first < len(casual) and casual[first] * 2 < score:
            remain = score - casual[first]
            second = first
            while second < len(casual) and casual[second] < remain:
                result += (remain - casual[second]) in doubles and 1 or 0
                second += 1
            first += 1
    print("The result is: {}".format(result))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))
