import random
a = random.randint(1,100)
x = 0
while x <=10:
	b = int(input('请输入数值'))
	if a>b:
		print('请输入的值与实际值偏小')
	elif a == b:
		print('猜对了')
	elif a<b:
		print('你输入的值与实际的值偏大')
	x+=1
