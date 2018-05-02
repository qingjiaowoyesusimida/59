def sum (a,b,*args,**kwargs):
	c=a+b
	print(a)
	print(b)
	print(args)
	print(kwargs)
	return c
t =(1,2,3,4,5,6)
d ={'age':18}
print (sum(1,2,*t,**d))
