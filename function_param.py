def print_max(a,b):
	if a>b:
		print(a,'is maximum')
	elif a==b:
		print(a,'is eaual to',b)
	else:
		print(b,'maximum')

print_max(3,4)

x=int(input('Enter first number:'))
y=int(input('Enter second number:'))

print_max(x,y)