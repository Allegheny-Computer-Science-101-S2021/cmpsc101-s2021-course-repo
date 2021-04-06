import array,sys
import numpy as np
a,b,c,d,e,f,g,h,i,j = 1,2,3,4,5,6,7,8,9,10
ls = [1,3,5,7,9]
print(id(ls))
for i in range(0,len(ls)):
	print(i, id(ls[i]),sys.getsizeof(ls[i]))	
print("-----------------------------------")
a,b,c,d,e,f,g,h,i,j = 11,12,13,14,15,16,17,18,19,20
#arr = array.array('i',[11,13,15,17,19])
arr = np.array([11,13,15,17,19],int)
print(arr.ctypes.data)
print(arr[0:1].ctypes.data, arr[0:1])
print(arr[1:2].ctypes.data, arr[1:2])
print(arr[2:3].ctypes.data, arr[2:3])
print(arr[3:4].ctypes.data, arr[3:4])
print(arr[4:5].ctypes.data, arr[4:5])




	


