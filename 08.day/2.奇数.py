i = 1
n = 0
while i<=100:
	if i%2 == 1:
		print('当前数字:%d'%i)
		i+=2
		n = i+n
print('求和是:%d'%n)

