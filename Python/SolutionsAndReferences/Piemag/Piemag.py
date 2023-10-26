
# start  list of all owl numbers (ie those which can be expressed 
# as the sum of a number and the sum of its digits)
owl_numbers = []

# for each integer, generate the sum of it and its sum-of-digits
for num in range(0,10000):

    # get the number in letters
    digits = str(num)

    # get the sum of the digits using comprehension
    sum_of_digits = sum([int(digit) for digit in digits])

    # add this to the original number, and add to list
    # if not already in it
    this_total = num + sum_of_digits
    if this_total not in owl_numbers:
        owl_numbers.append(this_total)

# for each integer, see if it's in list of owl numbers 
# (do in blocks of 100)
for number_digits in range(1, 10000, 100):

    # for each integer in this range which isn't in the list, get its string representation
    this_number_set = [str(n) for n in range(number_digits, number_digits + 99) if n not in owl_numbers]

    # join these together with commas
    number_block = ",".join(this_number_set)

    # print this block
    print(number_block)