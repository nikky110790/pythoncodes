from numpy import *

arr = array([1,4,7,5,89,34])

temp=0
for i in arr:
    if temp<i:
        temp=i

print ("The maximum in this array is - ",temp)