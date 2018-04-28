shoplist=['apple','mango','caroot','banana']
name='liaoyi'

print('Item 0 is:',shoplist[0])
print('Item 1 is:',shoplist[1])
print('Item 2 is:',shoplist[2])
print('Item 3 is:',shoplist[3])

print('Item -1 is:',shoplist[-1])
print('Item -2 is:',shoplist[-2])
print('Character 0 is:',name[0])

print('Item 1 to 3 is:',shoplist[1:3])
print('Item 2 to end is:',shoplist[2:])
print('Item 1 to -1 is:',shoplist[1:-1])
print('Item star to end is:',shoplist[:])

print('Character 1 to 3 is:',name[1:3])
print('Character 2 to end is:',name[2:])
print('Character 1 to -1 is:',name[1:-1])
print('Character star to end is:',name[:])

print(shoplist[::1])
print(shoplist[::2])
print(shoplist[::3])
print(shoplist[::-1])