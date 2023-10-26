# Create a program to store the olympics medals and to print it

# Import numpy
import numpy as np

# Store the medals tally
olympics_medals = np.array(
    [
        [1, 'United States', 39, 41, 33],
        [2, 'China', 38, 32, 18],
        [3, 'Japan', 27, 14, 17],
        [4, 'GBP', 22, 21, 22],
        [5, 'ROC', 20, 28, 23]
    ]
)

# Sliced array to remove the rank
sliced_array = olympics_medals[:, 1:]
# print(sliced_array)

for record in sliced_array:

    # Unpacking each rows
    country, gold, silver, bronze = record

    total_medals = int(gold) + int(silver) + int(bronze)

    print("{0:13} won a total of {1:3} medals of which {2} is gold, {3} is silver and {4} is bronze medals".format(
        country, total_medals, gold, silver, bronze))
