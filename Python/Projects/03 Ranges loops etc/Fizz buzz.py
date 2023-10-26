counter = 0

while True:

    counter += 1
    
    #test if gone too far
    if counter >= 100:
        break

    #if divisible by 3
    if counter % 3 != 0:
        continue
    
    print(counter, "fizz buzz")

print("That's it") 