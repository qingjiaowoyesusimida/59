def num(a,d,*args,**kwargs):
	all_num=0
	c=a+d
	print(a)
	print(d)
	print(args)
	print(kwargs)
	all_num+=c
	return c
	for i in args:
		all_num+=i
	for i in kwargs.values():
		all_args+=i
	print(all_num)
t=(3,4,5)
b={'age':18}
num(1,2,*t,**b)
	
