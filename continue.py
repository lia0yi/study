while True:
	s=input('Enter something:')
	if s=='quit'or s=='exit':
		break
	if len(s)<3:
		print('Too small')
		continue
	print('Input is of sufficient length')
print('Done')
