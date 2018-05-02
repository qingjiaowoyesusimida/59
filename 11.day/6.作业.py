x = []
l = []
ints = 3
while ints > 0:
	i = {}
	name = input('请输入名字')
	if name in l:
		print('姓名重复，请重新输入')
		continue
	l.append(name)
	age = input('请输入年龄:')
	sex = input('请输入性别:')
	qq = input('请输入QQ:')
	ti = input('请输入体重:')
	i['age'] = age
	i['sex'] = sex
	i['qq'] = qq
	i['ti'] = ti
	x.append(i)
	ints=ints-1
for k in x:
	print(k)

