print('学生成绩管理系统'.center(30,'*'))
print('1.录入成绩'.center(30,' '))
print('2.查询成绩'.center(30,' '))
print('3.修改成绩'.center(30,' '))
print('4.删除成绩'.center(30,' '))
print('5.打印全部成绩'.center(30,' '))
print('6.退出程序'.center(30,' '))
cards = []
while True:
	numder = int(input('请选择功能'))
	if numder == 1:
		print('录入')
		flag = 0
		card = {}
		xuehao = int(input('请输入学号'))
		for temp in cards:
			if xuehao == temp('xuehao'):
				flag = 1
				break
		if flag == 1:
			print('学号重复')
			continue
		name = input('请输入名字')
		kemu = input('请输入科目')
		result =int(input('请输入成绩'))
		card['xuehao'] = xuehao
		card['name'] = name
		card['kemu'] = kemu
		card['result'] = result
		cards.append(card)
		print('录入成功')
	elif numder == 2:
		print('查询')
		xuehao = int(input('请输入要查找的学号'))
		falg = 0
		count = 0
		for temp in cards:
			if xuehao == temp['xuehao']:
				count+=1
				falg = 1
				break
		if flag == 0:
			print('查无此人\n')
		else:
			print('学号:%s\n学生姓名:%s\n科目:%s\n分数:%S\n'%(cards[count-1]['xuehao'],cards[count-1]['name'],cards[count-1]['kemu'],cards[count-1]['result']))

