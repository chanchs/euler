import lib.utilities as ut
import math
import time


if __name__ == "__main__":
    start = time.time()

    max_k = 12000
    limit = 2 * max_k
    n = [2 * max_k for i in range(max_k)]

    def get_product_sum_number(num, sum_product, product, strt):
        """
        n = sum_product + product
        :param n:
        :param sum_product:
        :param product:
        :param start:
        :return:
        """
        k = num - sum_product + product
        if k < max_k:
            if num < n[k]:
                n[k] = num
            for i in range(strt, max_k // num * 2):
                get_product_sum_number(num * i, sum_product + i, product + 1, i)

    get_product_sum_number(1, 1, 1, 2)
    ans = sum(set(n[2:]))
    print(ans)

    end = time.time()
    print("Completed in {0:.2}s".format(end - start))

