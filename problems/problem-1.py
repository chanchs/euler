
class Problem1:

    def get_multiples_of_3_or_5(n):
        x = [i for i in range(1, n) if i % 3 == 0 or i % 5 == 0]
        return x

if __name__ ==  '__main__':
    P = Problem1

    num = P.get_multiples_of_3_or_5(1000)
    print(num)
    print("sum = {}".format(sum(num)))