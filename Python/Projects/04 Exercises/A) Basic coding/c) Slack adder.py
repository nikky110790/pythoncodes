
# Function to add 2 numbers
def AddTwoNumbers(a, b):
    return a + b

# Enter the first number
a = input("Enter the first number ===> ")
b = input("Think of another number ===> ")

c = AddTwoNumbers(int(a), int(b))

print("The sum of {0} and {1} is {2}".format(a, b, c))