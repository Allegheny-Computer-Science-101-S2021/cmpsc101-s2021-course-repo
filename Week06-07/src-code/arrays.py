import array, time, sys
import numpy as np
def generateArray(cap):
	start_time = time.time()	
	arr = array.array('i',[])
	for num in range(0,cap):
		arr.append(num)
	end_time = time.time()
	print("array generate took this long to run: {}".format(end_time-start_time))
	print("size of array:", sys.getsizeof(arr))
	return arr
def generateNPArray(cap):
	start_time = time.time()	
	arr = array.array('i',[])
	arr = np.arange(1,cap+1)
	end_time = time.time()
	print("np array generate took this long to run: {}".format(end_time-start_time))
	print("size of np array:", sys.getsizeof(arr))
	return arr
def generateList(cap):
	start_time = time.time()	
	ls = []
	for num in range(0,cap):
		ls.append(num)
	end_time = time.time()
	print("list generate took this long to run: {}".format(end_time-start_time))
	print("size of list:", sys.getsizeof(ls))
	return ls

def processArray(arr,cap):
	start_time = time.time()	
	for i in range(len(arr)):
		arr[i] = arr[i] + 100
	end_time = time.time()
	print("array process took this long to run: {}".format(end_time-start_time))

def processNPArray(arr,cap):
	start_time = time.time()	
	mod_arr = np.array(arr)
	mod_arr = mod_arr+100
	end_time = time.time()
	print("np array process took this long to run: {}".format(end_time-start_time))

def processList(ls,cap):
	start_time = time.time()	
	for i in range(0,cap):
		ls[i] = ls[i]+100
	end_time = time.time()
	print("list process took this long to run: {}".format(end_time-start_time))
	

cap = 10000000
arr = generateArray(cap)
np_arr = generateNPArray(cap)
ls = generateList(cap)
processArray(arr,cap)
processNPArray(np_arr,cap)
processList(ls,cap)

