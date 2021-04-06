def displayR(ls):
	for i in range(len(ls)):
		for j in range(len(ls[i])):
			print(ls[i][j],"\t",end='')
		print("")

def displayC(ls):
	row = 1
	for i in range(len(ls)):
		for j in range(len(ls[i])):
			print(ls[j][i],"\t",end='')
		print("")
ls = [[1,2,3,4,5],[6,7,8,9],[10,11,12],[13,14],[15]]
displayR(ls)
displayC(ls)