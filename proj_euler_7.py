from sys import argv
script, n = argv

def is_prime(num):
	flag = -1
	if num == 2 or num == 3:
		flag = 0
		return flag
	else:
		i = 2
		while i <= num/2:
			if num%i == 0:
				flag = 1
				break;
			else:
				flag = 0
			i += 1
		return flag
def nth_prime(x):
	count = 0
	for i in range(2,10000000000):
		ret = is_prime(i)
		if ret == 0:
			count +=1
		if count == x:
			break
		else:
			continue
	return i

ret = nth_prime(int(n))
print(ret)
