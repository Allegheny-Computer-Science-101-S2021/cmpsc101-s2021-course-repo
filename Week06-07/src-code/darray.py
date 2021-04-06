import array, time, sys, ctypes
import numpy as np
class darray:
	def __init__(self):
		self._size = 0   # total no of elements
		self._capacity = 1  # default array capacity
		self._arr = self._create_array(self._capacity) # create an array using low-level array
	def __str__(self):
		res = ""
		for i in range(self._size):
			res += str(i) + " "
		return res
		
	def __len__(self):
		# Return number of elements stored in the array.
		return self._size
	def __getitem__(self, k):
		# Return element at index k.
		if (k <= 0 and k > self._size):
			raise IndexError('invalid index')
		return self._arr[k] # retrieve from array
	def update(self, k, value):
		# Update the array
		self._arr[k] = value
	def append(self, obj):
		# Add object to end of the array
		if (self._size == self._capacity): # not enough room
			self._resize(2 * self._capacity) # so double capacity
		self._arr[self._size] = obj
		self._size += 1
	def _resize(self, c): # nonpublic utitity
		# Resize internal array to capacity c.
		temp = self._create_array(c)  # new (bigger) array
		for k in range(self._size):  # for each existing value
			temp[k] = self._arr[k]
		self._arr = temp # use the bigger array
		self._capacity = c
	def _create_array(self, c): # nonpublic utitity
		# Return new array with capacity c
		return (c * ctypes.py_object)()  # see ctypes documentation
	def insert(self, k, value):
		# Insert value at index k, shifting subsequent values rightward.
		# (for simplicity, we assume 0 <= k <= n in this verion)
		if self._size == self._capacity:    # not enough room
			self._resize(2 * self._capacity) # so double capacity
		for j in range(self._size, k, -1):  # shift rightmost first
			self._arr[j] = self._arr[j-1]
		self._arr[k] = value  # store newest element
		self._size += 1
	def remove(self, value):
    	# Remove first occurrence of value (or raise ValueError).
    	# note: we do not consider shrinking the dynamic array in this version
		for k in range(self._size):
			if self._arr[k] == value: # found a match!
				for j in range(k, self._size - 1): # shift others to fill gap
					self._arr[j] = self._arr[j+1]
				self._arr[self._size - 1] = None   # help garbage collection
				self._size -= 1                       # we have one less item
				return                             # exit immediately
		raise ValueError('value not found')    # only reached if no match

darr = darray()
# load darray
for i in range(5):
	darr.insert(i,i+1)
darr.append(6)
darr.remove(1)
# retrieve darray
for i in range(len(darr)):
	print(darr[i],"\t",end='')
print()
