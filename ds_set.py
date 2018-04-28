bri=set(['brazil','russia','india'])
if('india' in bri):
	print('india in bri')
else:
	print('india not in bri')

if('usa' in bri):
	print('usa in bri')
else:
	print('usa not in bri')

bric=bri.copy()
bric.add('china')
if(bric.issuperset(bri)):
	print('bric is the superset of bri')

bri.remove('russia')
print(bri & bric)
