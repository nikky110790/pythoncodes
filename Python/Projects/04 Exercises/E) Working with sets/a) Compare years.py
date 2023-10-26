# open the files in the folder and compare them and find the unique grand prix for each year

# opening the 2016 Grand Prix file and printing the values
import glob

grand_prix_list = []

with open(r"D:\My_Learning\Python\SolutionsAndFiles\GrandPrix\Grand Prix 2016.csv", "r") as grand_prix_2016:

    # Reading the data inside it
    lines = grand_prix_2016.read().splitlines()

    # Getting only Grand Prix names from each lines
    for line in lines:

        # Unpacking each line into variables
        grand_prix_number, grand_prix_name = line.split(",")

        grand_prix_list.append(grand_prix_name)

grand_prix_2016.close()

grand_prix_2016_set = set(grand_prix_list)

grand_prix_list = list(grand_prix_2016_set)

grand_prix_list.clear()

# opening the 2017 Grand Prix file and printing the values
with open(r"D:\My_Learning\Python\SolutionsAndFiles\GrandPrix\Grand Prix 2017.csv", "r") as grand_prix_2017:

    # Reading the data inside it
    lines = grand_prix_2017.read().splitlines()

    # Getting only Grand Prix names from each lines
    for line in lines:

    # Unpacking each line into variables
        grand_prix_number, grand_prix_name = line.split(",")

        grand_prix_list.append(grand_prix_name)

grand_prix_2017.close()

grand_prix_2017_set = set(grand_prix_list)

grand_prix_list = list(grand_prix_2017_set)

# Getting the unique grand prix from the year 2016
unique_grand_prix_year = grand_prix_2016_set - grand_prix_2017_set

# Printing the grand prix for year 2016
# for item in unique_grand_prix_year:

#     print("{0} is in 2016 only".format(item))

# # Getting the unique grand prix from the year 2017
# unique_grand_prix_year = grand_prix_2017_set - grand_prix_2016_set

# # Printing the grand prix for year 2016
# for item in unique_grand_prix_year:

#     print("{0} is in 2017 only".format(item))


# Fetching the symmetric difference
exception_list = grand_prix_2016_set ^ grand_prix_2017_set

# Printing the exception list
title = "Below are the exception list across the years:\n"
print(title + "-" * len(title))

for exception in exception_list:

    if exception in grand_prix_2016_set:
        print("{0} is in 2016 only".format(exception))
    elif exception in grand_prix_2017_set:
        print("{0} is in 2017 only".format(exception))


# Fetching the Intersection
intersection_list = grand_prix_2016_set & grand_prix_2017_set

# Printing the Intersection list
title = "\nBelow are the intersection list across the years:\n"
print(title + "-" * len(title))

for intersection in intersection_list:

    print("{0} is available in both 2016 and 2017".format(intersection))


# Fetching the Union
union_list = grand_prix_2016_set | grand_prix_2017_set

# Printing the Union list
title = "\nBelow are the union list across the years:\n"
print(title + "-" * len(title))

for union in union_list:
    
    print("{0} is grand prix events in both 2016 and 2017".format(union))