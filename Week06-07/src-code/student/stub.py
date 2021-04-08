from driver import driver
cap = int(input("Enter no of students:"))
driver = driver()
students = driver.load(cap)
driver.display(students)
