arr = [1,3,7,14,25,36,45,53,68,79,99,]
key = 25
min =0
max = len(arr) - 1
center = int((min+max)/2)
if key in arr:
	while True:
		if arr[center]>key:
			center = center - 1
		elif arr[center]<key:
			center = center + 1
		elif arr[center] ==key:
			print(str(key)+'在数组里面的第'+str(center)+'个位置')
			break
else:
	print('没有该数字')
