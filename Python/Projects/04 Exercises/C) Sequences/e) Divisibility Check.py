# In a new program, create a variable to hold the first 50 integers. 
# Loop over the values in this range, printing out those which are divisible by 3 but not by 2:


first_50_integers = range(1, 51)

for num in first_50_integers:
    if num % 3 == 0 and num % 2 != 0:
        print(num) 