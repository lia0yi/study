#	我会推荐你总是使用括号
#	来指明元组的开始与结束
#	尽管括号是一个可选选项。
#	明了胜过晦涩，显式优于隐式。
# tuple 一经定义就不能再改动
zoo=('python','elephant','penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo	= 'monkey','camel',	zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are',	new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))

# 不支持del操作
# del zoo[0]
# pring('the first item is:',new_zoo[2][0])

# “可变”tuple
t = ('a','b',['A','B'])
t[2][0]='X'
t[2][1]='Y'
t[2].append('Z')
print(t)