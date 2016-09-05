from sys import argv
from functools import reduce

def get_gcd(a,b):
    while b:
        a,b = b,a%b
    return a
def get_lcm(a,b):
    res = (a*b)/get_gcd(a,b)
    return res
def lcm(*args):
    return reduce(get_lcm,args)

ret = lcm(*range(1,20))
print(ret)
