from sys import argv
import math
script, n = argv


def is_palin(num):
    n = num
    rev = 0
    while num > 0:
        unit = num % 10
        rev = (rev * 10)+unit
        num = int(num/10)
    if rev == n:
        return 1
    else:
        return 0


def find_max_product(digits):
    res = 0
    for i in range(int(math.pow(10, digits-1)),int(math.pow(10, digits))):
        for j in range(int(math.pow(10, digits-1)),int(math.pow(10, digits))):
            prod = i * j
            ret = is_palin(prod)
            if ret == 1 and prod > res:
                res = prod
    return res

final = find_max_product(int(n))
print(final)
