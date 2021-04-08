class student:
	def __init__(self,studentid,studentname,studentgpa):
		self._studentid = studentid
		self._studentname = studentname
		self._studentgpa = studentgpa
	def getStudentID(self):
		return self._studentid
	def getStudentName(self):
		return self._studentname
	def getStudentGPA(self):
		return self._studentgpa