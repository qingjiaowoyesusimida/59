def check_phone(phone):
	if phone.startswith('1') and len(phone) == 1:
		return True
	else:
		return False
phone = input('请输入电话号')
result = check_phone(phone)
if resulf == False:
	print('手机号是错的')
phone2 == input('请输入手机号')
result = check_phone(phone2)
if result == False:
	print('手机号是错的')
