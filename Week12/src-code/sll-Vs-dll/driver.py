import time
from slink import slink
from dlink import dlink

'''
dll = dlink();
for no in range(1,11):
	dll.insertE(no)
for no in range(1,20):
	print(dll.searchF(no))
'''

no_of_nodes = int(input("Enter the number of nodes:"))
start_time = time.time()	
sll = slink();
for no in range(1,no_of_nodes):
	sll.insertE(no)
end_time = time.time()
print("sll insert took this long to run: {}".format(end_time-start_time))

start_time = time.time()	
dll = dlink();
for no in range(1,no_of_nodes):
	dll.insertE(no)
end_time = time.time()
print("dll insert took this long to run: {}".format(end_time-start_time))

#for no in range(no_of_nodes-1,0,-1):
#for no in range(1,no_of_nodes):
#for no in range(no_of_nodes-1,int(no_of_nodes/2),-1):
#for no in range(int(no_of_nodes/2),no_of_nodes):

start_time = time.time()	
for no in range(no_of_nodes-1,int(no_of_nodes/2),-1):
	sll.delete(no)
end_time = time.time()
print("sll delete took this long to run: {}".format(end_time-start_time))
#sll.display()

start_time = time.time()	
for no in range(no_of_nodes-1,int(no_of_nodes/2),-1):
	dll.delete(no)
end_time = time.time()
print("dll delete took this long to run: {}".format(end_time-start_time))
#dll.displayF()
