# Cheated :(
import lib.utilities as ut
import time


def is_square_anagram(w1, w2, squares):
    wr1 = list(w1)
    wr2 = list(w2)
    print(wr1, wr2)


if __name__ == '__main__1':
    start = time.time()

    squares = [i * i for i in range(35000)]

    with open("problem-98.txt") as f:
        for line in f:
            words = line.split(',')
    words = [word.replace('"', "") for word in words]

    l = len(words)
    sorted_words = []
    sorted_words = [sorted(word) for word in words]
    print(words)
    count = 0
    for i in range(l):
        for j in range(i + 1, l):
            if len(sorted_words[i]) == len(sorted_words[j]):
                is_equal = True
                for k in range(len(sorted_words[i])):
                    is_equal = sorted_words[i][k] == sorted_words[j][k]
                    if not is_equal:
                        break
                if is_equal:
                    count += 1
                    is_square_anagram(words[i], words[j], squares)

    print("count = {}".format(count))


    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

if __name__ == '__main__':
    start = time.time()

    W = {}

    words = eval('[' + open('problem-98.txt').read() + ']')

    for w in words:
        key = ''.join(sorted(w))
        W.setdefault(key, []).append(w)

    pairs = []

    for k in W:
        if len(W[k]) > 1:
            print(k, '->', W[k])
            pairs.append(W[k])

    maxSq, maxWord = 0, '?'

    for p in pairs:
        w0 = p[0]
        lw0 = len(w0)
        print('\nchecking', w0)

        for i in range(int((10 ** (lw0 - 1) ** .5) - 1), int((10 ** lw0 ** .5 + 1))):
            ii = i * i
            dii = ut.get_digits(ii)
            if len(dii) != lw0:
                continue
            z = zip(w0, dii)
            sz = set(z)

            if len(sz) == len(set([x[0] for x in sz])) == len(set([x[1] for x in sz])):
                print('coincide:', ii, w0)
                p1 = p[1:]
                dsz = dict(sz)
                for w1 in p1:
                    s = w1

                    for l in dsz:
                        s = s.replace(l, str(dsz[l]))

                    iis = int(s)
                    if ut.is_square(iis):
                        print('!!!FOUND:', w0, w1, ii, iis)
                        if max(ii, iis) > maxSq:
                            maxSq = max(ii, iis)
                            maxWord = w0 if ii > iis else w1

    print(maxSq, maxWord)
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

