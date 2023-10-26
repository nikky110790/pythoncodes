from array import *

arr=array('i',[])

n = int(input("Enter the number of array elements"))

for i in range(n):
    val = int(input("Enter the number"))
    arr.append(val)

print(arr)

k=0

s=int(input("Enter the number to find"))
for e in arr:
    if e==s:
        print(k)
    k+=1

print(arr.index(s))

from numpy import *

