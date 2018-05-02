#i = 1
#j = 1
#while i <=9:
	#while j<=9:
		#print('%d*%d=%d'%(i,j,i*j))
		#j+=1
	#print()
	#i+=1




i = 1
while i <=9:
	j =1
	while j<=i:
		print('%d*%d=%d\t'%(i,j,i*j),end=' ')
		j+=1
	print('')
	i+=1
