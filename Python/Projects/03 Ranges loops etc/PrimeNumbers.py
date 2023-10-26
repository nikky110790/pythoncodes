
# Algorithms to print the n number of primes

highest_number = 1000

for test_number in range(2, highest_number + 1):

    # print if the test number is 2, since it is the lowest prime number
    if test_number == 2:
        print(test_number)
        continue

    # Any other numbers until the higest number

    if_prime = True

    for possible_prime in range(2, test_number):
        
        # Testing whether the number is prime
        if test_number % possible_prime == 0:
            if_prime = False
            break

    if if_prime:
        print(test_number)

print("Thats it")