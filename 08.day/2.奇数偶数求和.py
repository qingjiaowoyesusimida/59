i = 0
n = 0
while i <=100:
	if i%2 == 0:
		print('当个数字:%d'%i)
		i+=2
		n = i + n
print('求和是%d'%n)

