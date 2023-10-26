# Calculating the series of pi value using leibniz formula

series_sum = 0.0
if_add = True
max_Series_Number = 500

# Looping over the range to get the series sum of pi

for i in range (1, max_Series_Number * 2, 2):

    if if_add:
        series_sum = series_sum + (1/i)
    else:
        series_sum -= (1/i)
    
    if_add = not if_add

    pi = 4 * series_sum

    print("After {0:3} iterations pi approximates to {1:7.10f}".format(i, pi))

