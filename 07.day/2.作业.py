nn = int(input('请输入年份'))
if nn%4 == 0 and nn%100 != 0 and nn%400 == 0:
	print('闰年')
else:
	print('平年')

