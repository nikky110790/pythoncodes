# Consolidating data from different worksheets into a single worksheet

# Importing the required libraries
import pandas as pd
import glob

# Creating the file path location
file_full_path = r"D:\My_Learning\Python\SolutionsAndReferences\Excel Consolidation\Consolidating Worksheets\SampleData_V1.0.xlsx"

# Creating a empty dataframe
consolidated_worksheets = pd.DataFrame()

# Loading the Excel workbook
sheets_dict = pd.read_excel(file_full_path, sheet_name=None)

for name, values in sheets_dict.items():
    
    # Appending the data
    consolidated_worksheets = pd.concat([consolidated_worksheets, values])

# Writing to a worksheet
consolidated_worksheets.to_excel(r'D:\My_Learning\Python\SolutionsAndReferences\Excel Consolidation\Consolidating Worksheets\Consolidated worksheets.xlsx', index = False)

print("Completed!!!!")