#Function to determine the square root of first 100 numbers

from math import sqrt

# for i in range(1, 101, 1):
#     print("The square root of {0:3} is {1:6.3f} ".format(i, sqrt(i)))

j = 1

while j <= 100:
    print("The square root of {0:3} is {1:6.3f} ".format(j, sqrt(j)))
    j = j + 1