list = [1,23,5,3,67,4,7,32]
for i in range(len(list)):
	for l in range(i+1,len(list)):
		if list[i]>list[l]:
			list[i],list[l] = list[l],list[i]
	print(list)
key = 4
min = 0
max = len(list)-1
center = int((min+max)/2)
if key in list:
	while True:
		if list[center]>key:
			center = center -1
		elif list[center]<key:
			center = center +1
		elif list[center]==key:
			print(str(key)+'在数组里面的第'+str(center)+'个位置')
			break
else:
	print('没有该数字')
