from link import link
sll = link();
for no in range(0, 10):
	sll.insert(no)
sll.display()

'''
sll.insertP(10,9.5)
sll.display()
'''

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