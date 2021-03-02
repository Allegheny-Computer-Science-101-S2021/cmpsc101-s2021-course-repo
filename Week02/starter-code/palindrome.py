def check(word):
	for item in range(0,int(len(word)/2)):
		if (word[item] != word[len(word)-item-1]):
			return False
	return True
word = input("Enter a word:")
if (check(word) == True):
	print("It's a palindrome!")
else:
	print("It's not a palindrome!")