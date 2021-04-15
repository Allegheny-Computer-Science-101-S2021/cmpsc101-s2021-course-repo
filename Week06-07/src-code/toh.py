# Recursive function to solve tower of hanoi puzzle 
# n number of disks
def toh(n, left, middle, right): 
    if (n > 0):
        #print(n,left,middle,right)
        toh(n-1, left, right, middle)
        print(f"Move disk {n} from rod {left} to rod {right}")
        toh(n-1, middle, left, right)
number_of_disks = 3 # Number of disks 
toh(number_of_disks, 'A', 'B', 'C') # A, B and C are names of rods 