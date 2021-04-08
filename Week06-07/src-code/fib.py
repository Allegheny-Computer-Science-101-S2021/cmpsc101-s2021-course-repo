def recursive_fib(num):
   if (num == 0 or num == 1):
       return num
   else:
       return recursive_fib(num-1) + recursive_fib(num-2)

num = int(input("Enter a no:"))
res = recursive_fib(num)
print(f"Final output:{res}")

