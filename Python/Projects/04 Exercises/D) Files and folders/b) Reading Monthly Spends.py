# Write a program to loop over all of the CSV files in the folder.  Your program should open each CSV file in turn, read in its lines (missing out the header row) and then add them to a list.

# Reading the files inside a folder

from datetime import datetime
import glob

# Create a variable to hold the folder path containing the list of files
print("Start Time {0}".format(datetime.now(), "dd-mm-yyyy hh:mm:ss"))

files = glob.glob(r"D:\My_Learning\Python\SolutionsAndFiles\ShoppingLists\\*.csv")

#Looping over each file in the folder
for file in files:
    
    # Printing the file name
    file_name = file.rpartition("\\")[2].split(".")[0]
    print(file_name)
    print("-" * len(file_name))

    # Opening the file and getting the data from it.
    with open(file, "r") as opened_file:
        
        # Reading the file line by line
        lines = opened_file.read().splitlines()[1:]

        # Printing the lines of the file
        for line in lines:
            
            # Unpacking the data into different variables
            shopping_date, shopping_shop, shopping_amount, = line.split(",")
            
            # Printing the data in the output window
            print(" on {0} spent {1:5.2f} in {2}".format(shopping_date, float(shopping_amount), shopping_shop))

    print("")
print("End Time {0}".format(datetime.now(), "dd-mm-yyyy hh:mm:ss"))