from stack.stack import stack
s = stack();
for no in range(0, 10):
	s.push(no)
s.display()
print(f"Top of the Stack:{s.top.getData()}")

# [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14] 15 pops
for no in range(0, 15):
	s.pop()
	s.display()
