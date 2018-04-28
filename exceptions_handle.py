try:
	text=iput('Enter something -->')
except EOFError:
	print('Why did you do an EOF on me?')
except KeyboardInterrupt:
	print('You cancaled the operation')
else:
	print('You entered {}'.format(text))