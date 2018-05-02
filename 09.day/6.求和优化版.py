a = int(input('请输入一个数字'))
s = int(input('请输入两个数字'))
k = 1
while True:
	print('请重新输入')
	a = int(input('请输入第一个数字'))
	s = int(input('请输入第二个数字'))
	z = 0
	if a < s:
		for a in range(a,s+1):
				print(a)
		break

