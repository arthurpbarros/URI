t = int(input())
for i in range(t):
    n = int(input())
    a = 0
    b = 1
    total = 0
    if (n == 0):
        print ("Fib(0) = 0")
    elif (n == 1):
        print ("Fib(1) = 1")
    else:
        for i in range(2,n+1,1):
            total = a + b
            a = b
            b = total
        print ("Fib({}) = {}".format(n,total))
