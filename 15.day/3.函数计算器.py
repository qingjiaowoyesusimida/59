def jisuanqi(x,y,z):
	if i == 1:
		z = x-y
		print('两数之差是%0.2f'%z)
	elif i == 2:
		z = x+y
		print('两数之和是%0.2f'%z)
	elif i == 3:
		z = x*y
		print('两数之积是%0.2f'%z)
	elif i == 4:
		if y != 0:
			z = x/y
			print('两数之商是%0.2f'%z)
		else:
			print('输入不合法')
while True:
	x = float(input('请输入一个数字'))
	y = float(input('请输入另一个数字'))
	i = int(input('请输入:1.- 2.+ 3.* 4./'))
	jisuanqi(x,y,i)
