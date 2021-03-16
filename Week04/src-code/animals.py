from abc import ABC, abstractmethod 
class animal(ABC): 
	@abstractmethod
	def sound(self):
		pass	
class cat(animal):
	def sound(self):
		print("meow")		
class lion(animal):
	def sound(self):
		print("roar")
class horse(animal):
	def sound(self):
		print("neigh")
class dog(animal):
	def sound(self):
		print("bark")
cat = cat()
cat.sound()
dog = dog()
dog.sound()

