grades = []
def print_menu():
	print('学生管理系统1.0'.center(30,'*'))
	print('1.新增学生信息'.center(30,' '))
	print('2.查询学生信息'.center(30,' '))
	print('3.修改学生信息'.center(30,' '))
	print('4.删除学生信息'.center(30,' '))
	print('5.全部学生信息'.center(30,' '))
	print('6.退出学生系统'.center(30,' '))
def input_grade():
	while True:
		fun_num =int(input('请选择功能'))
		if fun_num == 1:
			add_grade()
		elif fun_num == 2:
			find_grade()
		elif fun_num == 3:
			update_grade()
		elif fun_num == 4:
			del_grade()
		elif fun_num == 5:
			all_grade()
		else:
			break
def add_grade():
	grade ={}
	number =int(input('请输入学号'))
	name = input('请输入名字')
	class_n = input('请输入班级')
	score =int(input('请输入成绩'))
	grade['number'] = number
	grade['name'] = name
	grade['class_n'] = class_n
	grade['score'] = score
	grades.append(grade)
	print('新增成功')
def find_grade():
	number = int(input('请输入学号'))
	flag = 0
	for temp in grades:
		if number == temp['number']:
			flag =1
			print('学号:%s\n名字:%s\n班级:%s\n成绩:%s\n'%(temp['number'],temp['name'],temp['class_n'],temp['score']))
		else:
			print('查无此人')
def update_grade():
	number = int(input('请输入要修改的学号'))
	falg = 0
	for temp in grades:
		if number == temp['number']:
			flag = 1
			print('1:修改名字')
			print('2:修改班级')
			print('3:修改成绩')
			update_grade = int(input('请输入要修改的选项'))
			if update_grade ==1:
				new_name =input('请输入新的名字')
				temp['name'] = new_name
			elif update_grade ==2:
				new_class_n = input('请输入新的班级')
				temp['class_n'] = new_class_n
			elif update_grade ==3:
				new_score = int(input('请输入新的成绩'))
				temp['score'] = new_score
			else:
				print('输入有误')
	if flag ==0:
		print('查无此人')
def del_grade():
	number = int(input('请输入要删除学生的学号'))
	flag = 0
	for temp in grades:
		if number == temp ['number']:
			flag =1
			sure_num = int(input('1.确定删除 2.取消删除'))
			if sure_num ==1:
				grades.remove(temp)
				print('删除成功')
			break
	if flag ==0:
		print('查无此人')
def all_grade():
	print('学号:'.center(8,' '),end=' ')
	print('名字:'.center(8,' '),end=' ')
	print('班级:'.center(8,' '),end=' ')
	print('成绩:'.center(8,' ' ))
	for temp in grades:
		print(str(temp['number']).center(8,' '),end=' ')
		print(temp['name'].center(8,' '),end=' ')
		print(temp['class_n'].center(8,' '),end=' ')
		print(str(temp['score']).center(13,' '))
def end_grade():
	print('感谢使用')
print_menu()
input_grade()
end_grade()
