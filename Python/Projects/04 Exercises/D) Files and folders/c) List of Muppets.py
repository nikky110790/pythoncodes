# Working on csv files to list the muppets

# creating a variable for the file path

with open(r"D:\My_Learning\Python\SolutionsAndFiles\List of Muppets\Muppets.csv","r") as muppet_file:

    # Read the csv file
    lines = muppet_file.read().splitlines()
    
    # Iterating each line in the lines
    for line in lines:
        
        # Unpacking the read lines to variables
        muppet, animal, colour = line.split(",")

        # Printing the unpacked cells in the line wiht desired format
        print("{0} ({1} {2})".format(muppet, colour, animal))

muppet_file.close()