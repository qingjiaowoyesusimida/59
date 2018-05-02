def nianling():
	if age <2:
		print('婴儿')
	elif age >=2 and age <4:
		print('学步')
	elif age >=4 and age <13:
		print('儿童')
	elif age >=13 and age <25:
		print('少年')
	elif age >=25 and age <50:
		print('青年')
	elif age >=50 and age <80:
		print('老年')
	elif age >80:
		print('长寿老人')
age=int(input('请输入年龄'))
nianling()
