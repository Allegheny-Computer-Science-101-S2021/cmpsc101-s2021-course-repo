class student:
	def __init__(self,id,name,gpa):
		self.id = id
		self.name = name
		self.gpa = gpa
	def report(self):
		print("-----------------------")
		print("Student Id:", self.id)
		print("Student Name:", self.name)
		print("Student GPA:", self.gpa)
		print("-----------------------")

