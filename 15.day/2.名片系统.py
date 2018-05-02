cards = []
def print_menu():
	print('名片系统v0.1版本'.center(30,'*'))
	print('1.新增名片'.center(30,' '))
	print('2.查找名片'.center(30,' '))
	print('3.修改名片'.center(30,' '))
	print('4.删除名片'.center(30,' '))
	print('5.退出'.center(30,' '))
def input_fun():#查找名片
	while True:
	fun_numder = int(input('请选择功能'))
	if fun_numder ==1:
		add_card()
	elif fun_numder ==2:
		add_card()
	elif fun_numder ==3:
		add_card()
	elif fun_numder ==4:
		add_card()
	elif fun_numder ==5:
		add_card()
	else:
		break
def add_card():#新增名片
	card = {}
	jod = input('请输入职业')
	phone = int(input('请输入手机号'))
	company = input('请输入公司名字')
	card['name'] = name
	card['jod'] = jod
	card['phone'] = phone
	card['company'] = company
	cards.append(card)
	print('新增成功')
	print(cards)
def find_card():#修改名片
	name = input('请输入要修改的名字')
	for temp in cards:
		flag = 1
		if name == temp['name']
			print('1.修改名字')
			print('2.修改职业')
			print('3.修改电话')
			print('4.修改公司')
			update_num =int(input('请输入要修改的选项'))
			if update_num == 1:
				new_name = input('请输入新的名字:')
				temp['name'] ==new_name
			elif update_num = 2:
				new_jod = input('请输入新的职位')
				temp['jod'] == new_jod
			elif update_num = 3:
				new_phone =int(input('请输入新的手机号'))
				temp['phone'] == new_phone
			elif update_num = 4:
				new_ company = input('请输入新的公司')
				temp['company'] == new_company
			else:
				print('输入有误')
	if flag ==0:
		print('查无此人')
def del_card():#删除名片
	name = input('请输入要删除的名字')
	falg=0
	for temp in cards:
		if name == temp['name']
			falg = 1
			cards.remove(temp)
	if flag ==0:
		print('查无此人')
def all_card():#打印名片
	print('名字\n职位\n公司\n手机号')
	for temp in cards:
		print('%s\n%s\n%s\n%d'%(temp['name'],temp['jod'],temp['company'],temp['phone']))
print_menu()
input_fun()
	else:
		print('再见')
		break
