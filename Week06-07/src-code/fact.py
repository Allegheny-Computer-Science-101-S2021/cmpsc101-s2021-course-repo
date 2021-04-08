def recursive_fact(num):
   if num == 1:
       return num
   else:
       return num*recursive_fact(num-1)

num = int(input("Enter a no:"))
res = recursive_fact(num)
print(f"Final output:{res}")

