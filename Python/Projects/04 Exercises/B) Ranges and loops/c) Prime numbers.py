# Function to create a prime number

highest_number = 10000

print("The list of prime numbers till {0} are below ".format(highest_number))

for i in range (2, highest_number + 1):

    if i == 2:
        print(i)
        continue

    if_prime = True

    for j in range (2, i):

        if i % j == 0:
            if_prime = False
            break

    if if_prime:
        print(i)