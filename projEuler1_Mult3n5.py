#Project Euler 1
from sys import argv
script, num = argv

def mult_3n5 (number):
    sum = 0
    n = 0
    while n < number:
        if n%3 == 0:
            sum += n
        elif n%5 == 0:
            sum += n
        n += 1
    return sum

ret = mult_3n5(int(num))
print(ret)
