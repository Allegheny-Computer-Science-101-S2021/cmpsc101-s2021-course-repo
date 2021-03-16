first = int(input("Enter first:"))
second = int(input("Enter second:"))
try:
    divide = first/second
    print(divide)
except ZeroDivisionError:
    print ("WARNING: Invalid Equation")
