def print_max(x,y):
	'''打印两个数值中最大的。

	这两个数都应该是整数'''
	x=int(x)
	y=int(y)

	if x>y:
		print(x,'is maxium')
	else:
		print(y,'is maxium')

print_max(3,5)
print(print_max.__doc__)