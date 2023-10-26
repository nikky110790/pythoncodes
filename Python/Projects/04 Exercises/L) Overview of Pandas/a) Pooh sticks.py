# Importing the pandas

from pandas import *

# Reading the Excel workbook and printing it
pooh_workbook = read_excel(r"D:\My_Learning\Python\SolutionsAndReferences\Pooh\Pooh.xlsx")

# Loading the data into the dataframe
data = DataFrame(pooh_workbook)

# Soritng the dataframe based on max pooh sticks
sorted_data = data.sort_values(
    ["Poohsticks score", "Matches Played"]
    ,ascending = False
)

# Printing the first 3 rows in the sorted data
sorted_data = sorted_data.head(3)

# Renaming the clolumn headers in the data frame
new_pooh_data = data.rename(columns =
    {
        "Name" : "Character",
        "Poohsticks score" : "Score",
        "Matches Played" : "Played"
    }
)

# Generating the statistics for the new dataframe
print(new_pooh_data.agg(
        {
            "Score" : ["min", "max", "median", "mean", "count", "nunique"],
            "Played" : ["min", "max", "mean", "median", "count", "nunique"]
        }
    )
)