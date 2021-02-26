def fib(r):
    a = 0
    b = 1

    print(a)
    print(b)

    for i in range(r):
        temp = a  # temp = 2
        a = b  # a = 3
        b = temp + a  # 5
        print(b)


# 0 1 1 2 3 5

fib(4)
