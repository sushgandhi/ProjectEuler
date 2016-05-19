from sys import argv

script, num = argv
def square_diff(n):
    sum_sq = 0
    sum = 0
    for i in range(n+1):
        temp = i * i
        sum_sq += temp
        sum += i
    diff = (sum*sum)-sum_sq
    return diff

ret = square_diff(int(num))
print(ret)
