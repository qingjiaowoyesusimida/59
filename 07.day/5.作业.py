acc = input('请输入账号')
passmd = input('请输入密码')
if acc =='123456' and passmd =='adc': 
	print('登入成功')
elif acc != '123456' and passmd =='adc':
	print('账号不对')
elif acc =='123456' and passmd != 'adc':
	print('密码不对')
 
