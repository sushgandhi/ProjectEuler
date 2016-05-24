from sys import argv
from math import sqrt
script, num = argv
def prime_factors(n):
    prime_factor = []
    i = 3
    while n%2 == 0:
        prime_factor.append(2)
        n = n/2
    while i<=sqrt(n):
        while n%i == 0:
            prime_factor.append(i)
            n = n/i
        i = i +2
    if n >2 :
        prime_factor.append(n)

    largest = max(prime_factor)
    return largest

ret = prime_factors(int(num))
print(ret)
