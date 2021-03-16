class car:
	def __init__(self,model,odometer,fuel,mpg):
		self.__model = model
		self.__odometer = odometer
		self.__fuel = fuel
		self.__mpg = mpg
	
	def fuel_tank(self,miles):
		fuel_required = miles/self.__mpg
		if (self.__fuel >= fuel_required):
			return True
		else:
			return False
	
	def fillup(self):
		self.__fuel = 10

	def drive(self,miles):
		if (self.fuel_tank(miles)):
			print(f"trip start:\t{self.__odometer}")
			self.__odometer = self.__odometer + miles
			self.__fuel = self.__fuel - (miles / self.__mpg)
			print(f"trip end:\t{self.__odometer}")
		else:
			print("\tGAS STOP")
			self.fillup()
			self.drive(miles)
	

c1 = car("civic",10000,10.34,22.34)
c1.drive(100)
c1.drive(100)
c1.drive(100)
