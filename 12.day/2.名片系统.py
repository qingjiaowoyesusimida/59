print('名片系统v0.1版本'.center(30,'*'))
print('1.新增名片'.center(30,' '))
print('2.查找名片'.center(30,' '))
print('3.修改名片'.center(30,' '))
print('4.删除名片'.center(30,' '))
cards = []
while True:
	l = int(input('请选择功能'))
	if l ==1:
		print('新增')
		flag = 0
		card ={}
		name = input('请输入名字')
		for x in cards:
			if name == x['name']:
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
	elif l == 2:
		print('查找')
	elif l == 3:
		print('修改')
	elif l == 4:
		print('删除')
