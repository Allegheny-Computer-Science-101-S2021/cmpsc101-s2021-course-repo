from link import link
#Use the Student class to create an object, and then execute the printname method:
sll = link();
for no in range(0, 10):
	sll.insert(no)
sll.display()

'''
# print head
print(sll.head.getData())
'''

''' 
# delete in reverse order. 
for no in range(0,10):
	sll.delete(no)
sll.display()
'''

''' 
# delete in forward order. 
for no in range(9,-1,-1):
	sll.delete(no)
sll.display()
'''