# coding=UTF-8
class SchoolMember:
	'''代表任何学校里的成员。'''
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print('(Initializing SchoolMember:{})'.format(self.name))

	def tell(self):
		'''告诉我有关我的细节。'''
		print('Name:"{}"Age:"{}"'.format(self.name,self.age),end=" ")


class Teacher(SchoolMember):
	'''代表一位老师。'''
	def __init__(self,name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary=salary
		print('(Initialized Teacher: {})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Salary:"{:d}"'.format(self.salary))

class Sdudent(SchoolMember):
	'''代表一位学生。'''
	def __init__(self, name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks=marks
		print('(Initialized Sdudent: {})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks:"{}"'.format(self.marks))
		

s=Sdudent('liaoyi',25,75)
t=Teacher('Mrs.Zhang',46,30000)

print()

members=[t,s]
for member in members:
	#	对全体师生工作
	member.tell()