# Reading the worlds tallest buildings from csv file and printing them

# Creating Print Title Function
def print_title(title:str) -> str:
    return title + "\n" + "-" * len(title)

# Creating a dictionary variable to store the details retrieved from thee csv file
tallest_buildings_dict = {}


# Open the csv file containing the details and fetch the data from it
with open(r"D:\My_Learning\Python\SolutionsAndReferences\Worlds Tallest Buildings\Tallest_Buildings.csv", "r") as tallest_buildings:

    # Reading the data from the input file
    lines = tallest_buildings.read().splitlines()[1:]

    # Iterating the lines and populating the dictionary
    for line in lines:

        #unpacking the details into each variables
        rank, name, city, country, metres = line.split(",")

        tallest_buildings_dict[name] = [rank, city, country, metres]

tallest_buildings.close()

# Printing the title of the data
print(print_title("The list of top 6 tallest buildings in the world"))

# Printing the details fetched from the input csv file
for key, value in tallest_buildings_dict.items():

    # Printing the details in the required format
    print("{0} in {1} is {2} metres high".format(key, value[1], value[3]))