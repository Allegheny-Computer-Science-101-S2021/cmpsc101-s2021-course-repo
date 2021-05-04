from link import link
dll = link();
for no in range(0, 10):
	dll.insertF(no)
dll.displayF()

'''
dll.insertP(10,0.5)
dll.displayR()
'''

'''
# print head
print(dll.head.getData())
'''

'''
# delete in reverse order. 
for no in range(0,10):
	dll.delete(no)
dll.displayR()
'''

'''
# delete in forward order. 
for no in range(9,-1,-1):
	dll.delete(no)
dll.displayR()
'''