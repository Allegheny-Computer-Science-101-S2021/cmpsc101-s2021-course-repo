import random
from student import student
class driver:
	def load(self,cap):
		obj = []
		for i in range(cap):
			s_id = i+1
			s_name = "S" + str(i)
			s_gpa = round(random.uniform(2,4),2)
			obj.append(student(s_id,s_name,s_gpa))
		return obj
	def display(self,obj):
		for i in range(len(obj)):
			print(obj[i].getStudentID(),"\t",obj[i].getStudentName(),"\t",obj[i].getStudentGPA())


