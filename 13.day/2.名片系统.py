print('名片系统v0.1版本'.center(30,'*'))
print('1.新增名片'.center(30,' '))
print('2.查找名片'.center(30,' '))
print('3.修改名片'.center(30,' '))
print('4.删除名片'.center(30,' '))
print('5.退出'.center(30,' '))
cards = []
while True:
	fun_numder = int(input('请选择功能'))
	if fun_numder ==1:
		print('新增')
		flag = 0
		card ={}
		name = input('请输入名字')
		for temp in cards:
			if name == temp['name']:
				flag = 1
				break
		if flag == 1:
			print('名字重复了')
			continue
		jod = input('请输入职业')
		phone = int(input('请输入手机号'))
		company = input('请输入公司名字')
		address = input('请输入公司地址')
		card['name'] = name
		card['jod'] = jod
		card['phone'] = phone
		card['company'] = company
		card['address'] = address
		cards.append(card)
		print('新增成功')
	elif fun_numder == 2:
		print('查找')
		name = input('请输入要查找的人')
		falg= 0
		count = 0
		for temp in cards:
			if name == temp['name']:
				count+=1
				flag = 1
				break
		if flag == 0:
			print('查无此人\n')
		else:
			print('姓名:%s\n职位:%s\n手机号:%s\n公司:%s\n地址:%s\n'%(cards[count-1]['name'],cards[count-1]['jod'],cards[count-1]['phone'],cards[count-1]['company'],cards[count-1]['address']))
	elif fun_numder == 3:
		print('修改')
		name = input('请输入要修改的人员')
		for temp in cards:
			if name == temp['name']:
				print('1:修改名字'.center(32,'*'))
				print('2:修改职位'.center(32,'*'))
				print('3:修改电话'.center(31,'*'))
				print('4:修改公司名字'.center(30,'*'))
				print('5:修改公司地址'.center(30,'*'))
				ge_num =int(input('请输入修改的内容:'))
				if ge_num == 1:
					name = input('请输入新的名字:')
					temp['name'] = name
				elif ge_num == 2:
					job = input('请输入新的职位:')
					temp['job'] = job
				elif ge_num == 3:
					phone = input('请输入新的手机号:')
					temp['phone'] = phone
				elif ge_num == 4:
					company = input('请输入新的公司名称:')
					temp['company'] = company
				elif ge_num == 5:
					addreess = input('请输入新的公司地址:')
					temp['address'] = address
				else:
					print('输入有误')
	elif fun_numder == 4:
		print('删除')
		name = input('请输入要删除的名字')
		for temp in cards:
			if name == temp['name']:
					flag = 1
					fun_numder == int(input('1.确认删除 2.返回'))
			if fun_numder == 0:
				cards.remove(temp)
				print('删除成功')
			break
		if flag == 0:
			print('查无此人')
	else:
		print('再见')
		break
