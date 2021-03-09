temp = input("Enter the temperature:")
temp = int(temp)
if (temp > 80):
	print("It's hot!")
elif (temp > 60 and temp < 80):
	print("It's mild!")
else:
	print("It's cold!")