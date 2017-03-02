import time

start = time.time()
ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
eleven_to_fifteen = ["eleven", "twelve", "thirteen", "fourteen", "fifteen"]
tens = ["teen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundred = ["hundred"]
thousand = ["thousand"]
and_v = "and"


def ret_ones(n):
    number = ""
    if n <= 10:
        number = ones[n - 1]
    elif 10 < n <= 15:
        number = eleven_to_fifteen[n - 11]
    elif 15 < n <= 19:
        if n == 18:
            number = ones[n - 16 + 5][:-1] + tens[0]
        else:
            number = ones[n - 16 + 5] + tens[0]
    elif 20 <= n < 100:
        d0 = n % 10
        d1 = int(n / 10)
        if d0 == 0:
            number = tens[d1 - 1]
        else:
            number = tens[d1 - 1] + " " + ones[d0 - 1]
    return number


if __name__=="__main__":
    n = 1000
    s = 0

    for i in range(1, n + 1):
        if i < 100:
            number = ret_ones(i)
        elif 100 <= i < 1000:
            d0 = i % 100
            d1 = int(i / 100)
            if d0 == 0:
                number = ret_ones(d1) + " hundred"
            else:
                number = ret_ones(d1) + " hundred " + and_v + " " +  ret_ones(d0)
        if 1000 <= i:
            d0 = i % 1000
            d1 = int(i / 1000)
            if d0 == 0:
                number = ret_ones(d1) + " thousand"

        l = len(number) - number.count(" ")
        s += l
        print("i = {0}, {1}, len = {2}, s = {3}".format(i, number, l, s))

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))