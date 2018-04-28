name='liaoyi'

if name.startswith('lia'):
	print('Yes, the string stars with "lia"')
if 'o' in name:
	print('Yes, it contains the string "o"')
if name.find('oy')!=-1:
	print('Yes, it contains the string "oy"')

delimiter='_*_'
mylist=['Brazil','Russia','India','China']
print(delimiter.join(mylist))