class person:
	"""hahaha"""
	def __init__(self,name):
		self.name=name

	def say_hi(self):
		print("hello,my name is",self.name)

	def __str__(self):
		print("the string in __str__")

p=person("Liaoyi")
p.say_hi()
print(p.__doc__)
#	前面两行同时也能写作
#	person('Swaroop').say_hi()