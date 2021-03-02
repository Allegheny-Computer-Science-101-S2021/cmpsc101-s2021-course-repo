number = input("Enter a phone number:")
number = int(number)
digits = 1
while(True):
	number = int(number/10)
	if (number <= 0):
		break
	else:
		digits = digits+1
if (digits == 10):
	print("It's a valid phone number!")
else:
	print("It's an invalid phone number!")