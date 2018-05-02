l = []
s = []
count = 0
while True:
	if count == 3:
		break
	x ={}
	for i in l:
		s.append(i.get('name'))
	name = input('请输入姓名')
	age = int(input('请输入年龄'))
	sex = input('请输入性别')
	qq = int(input('请输入QQ'))
	ti = float(input('请输入体重'))
	if name not in s:
		x['name'] = name
		x['age'] = age
		x['sex'] = sex
		x['qq'] = qq
		x['ti'] = ti
		l.append(x)
		s.append(name)
		print(l)
		count+=1
else:
		print('名字重复')
age_sum = 0
for i in l:
	age_sum = age_sum+i.get('age')
	print(i)
print('年龄的平均值是%0.2f'%(age_sum/len(l)))

