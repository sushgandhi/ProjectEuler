#Project Euler 2
from sys import argv
script, num = argv
def fibonacci(n):
    a = 1
    b = 2
    sum = 0
    while True:
        if  b>= n:
            break;
        if b%2 == 0:
            sum += b
        c = a+b
        a = b
        b = c
        print(b)
    return sum

ret = fibonacci(int(num))
print(' ')
print(ret)
