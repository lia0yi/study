#part1 print hello world!!!
print("hello world!!!")
#part1 format control

'''这是一段多行字符串。这是它的第一行。
This	is	the	second	line.
"What's	your	name?,"	I	asked.
He	said	"Bond,	James	Bond."
'''
age=20
name='liaoyi'
print('{0} was {1} years old when he wrote this book'.format(name,age))
print('Why is {0} playing with that python?'.format(name))

age=20
name='Swaroop'

print('{}	was	{}	years	old	when	he	wrote	this	book'.format(name,	age))
print('Why	is	{}	playing	with	that	python?'.format(name))

#	对于浮点数	'0.333'	保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
#	使用下划线填充文本，并保持文字处于中间位置
#	使用	(^)	定义	'___hello___'字符串长度为	11
print('{0:_^11}'.format('hello'))
#	基于关键词输出	'Swaroop	wrote	A	Byte	of	Python'		
print('{name} wrote {book}'.format(name='liaoyi',	book='A	Byte	of	Python'))
#	注意	print总是会以一个不可见的“新一行”字符（\n	）
print('c',end='')
print('f',end='')
print('x',end='')

#	变量
i=5
print(i)
i=i+1
print(i)
s='''This is a multi-line string.
This is the second line.'''
print(s)

s='This is a string. \
This continues the string.'
print(s)