import time
from stack.stack import stack
from que.queue import queue 
no_of_nodes = int(input("Enter the number of nodes:"))
start_time = time.time()	
s = stack();
for no in range(1,no_of_nodes):
	s.push(no)
end_time = time.time()
print("stack push took this long to run: {}".format(end_time-start_time))

start_time = time.time()	
q = queue();
for no in range(1,no_of_nodes):
	q.enqueue(no)
end_time = time.time()
print("queue enqueue took this long to run: {}".format(end_time-start_time))

start_time = time.time()	
for no in range(1,no_of_nodes):
	s.pop()
end_time = time.time()
print("stack pop took this long to run: {}".format(end_time-start_time))
start_time = time.time()	
for no in range(1,no_of_nodes):
	q.dequeue()
end_time = time.time()
print("queue dequeue took this long to run: {}".format(end_time-start_time))