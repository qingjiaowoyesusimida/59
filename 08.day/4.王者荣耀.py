acc = '396864068' 
passwd = '123456'
count = 1 
while True:
	account = input('请输入你的账号') 
	password = input('请输入你的密码')
	if account == acc and password == passwd:
		print('登录成功')
		choose_login = int(input('请选择你的英雄范围 0=ADC 1=肉　3=法师'))
		if choose_login == 0:
			print('鲁班大师')
		elif choose_login == 1:
			print('程咬金')
		elif choose_login == 3:
			print('王昭君')
		break
	else:
		print('错误%d次'%count)
		count+=1
		if count == 4:	
			print('账号冻结至2118年')
			break
	
	
 
