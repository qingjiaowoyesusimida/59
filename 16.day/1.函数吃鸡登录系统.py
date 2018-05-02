def register(phone,password):
	result = condition(phone)
	if result == True:
		print('注册成功')
	else:
		print('注册失败')
def logon(phone,password):
	result = condition(phone)
	if result == True:
		print('登录成功')
	else:
		print('登录失败')
def condition(phone):
	if phone.rtatsuith('1') and len(phone) == 11:
		return True
	else:
		return False
phone = input('请输入手机号')
password = input('请输入密码')
register(phone,password)
logon(phoone,password)

