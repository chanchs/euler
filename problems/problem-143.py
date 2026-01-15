import lib.utilities as ut
import math
import time

if __name__ == "__main__":
    start = time.time()
    Limit = 120000
    sq_Limit = int(round(math.sqrt(Limit)))
    # Store pairs in here
    pairs = []

    # Use the parameterization

    for u in range(1, sq_Limit):
        for v in range(1, u):
            if ut.gcd(u, v) != 1:
                continue
            if (u - v) % 3 == 0:
                continue
            a = 2 * u * v + v * v
            b = u * u - v * v

            if a + b > Limit:
                break
# From coprime pairs make composite pairs
            k = 1
            while k * (a + b) < Limit:
                pairs.append((k * a, k * b))
                pairs.append((k * b, k * a))
                k += 1

# Sort pairs list
    pairs.sort()

# Create index
    index = [-1] * Limit

    for i, (first, _) in enumerate(pairs):
        if index[first] == -1:
            index[first] = i

# Which sums have been reached?
    sums = [False] * Limit

 # Iterate through all pairs
    for i in range(len(pairs)):
        a, b = pairs[i]

# Construct vectors for indices
        va = []
        vb = []

 # Fetch indices
        ia = index[a]
        ib = index[b]

        while ia < len(pairs):
            next_first, next_second = pairs[ia]

            if next_first != a:
                break
            va.append(next_second)
            ia += 1

        while ib < len(pairs):
            next_first, next_second = pairs[ib]

            if next_first != b:
                break
            vb.append(next_second)
            ib += 1

 # Find common objects between va and vb

        for c_a in va:
            for c_b in vb:
                if c_a == c_b:
                    c = c_a
                    if a + b + c < Limit:
                        sums[a + b + c] = True

# Tally up sums
    s = sum(i for i in range(Limit) if sums[i])
    print(s)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

