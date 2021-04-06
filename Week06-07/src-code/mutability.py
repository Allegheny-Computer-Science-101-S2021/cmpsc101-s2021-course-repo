import array, numpy as np
x = 10
print(id(x))
x = 20
print(id(x))
y = 10
print(id(y))

ls = [1,2,3,4,5]
print(id(ls))
ls.append(6)
print(id(ls))

arr = array.array('i',[11,12,13,14])
print(id(arr))
arr.append(15)
print(id(arr))

np_arr = np.arange(21,25)
print(id(np_arr))
np.append(np_arr,26)
print(id(np_arr))
