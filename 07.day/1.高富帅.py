height = int(input('请输入身高'))
money = int(input('请输入身价'))
gg = int (input('请输入颜值分'))
if height >=175 and money >10000000000 and gg >99:
	print('高富帅')
elif money >100000000 and gg >99:
	print('富帅')
elif height <175 and money >1000 and gg >80:
	print('你就是个屌丝')
