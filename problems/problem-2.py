from lib.utilities import fibonacci_generative_to_n

if __name__=="__main__":
    print("hello world")
    sum = 0

    for i in fibonacci_generative_to_n(35):
        if i < 4000000:
            print(i)
            if i%2 == 0:
                sum += i
        else:
            break

    print("sum = {0}".format(sum))