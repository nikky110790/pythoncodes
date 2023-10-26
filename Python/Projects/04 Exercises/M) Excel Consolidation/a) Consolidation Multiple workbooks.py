# Consolidating multiple workbooks into single workbook

# Importing the required libraries
import pandas as pd
import glob

# Creating a folder location to loop for files
files = glob.glob(pathname = r'D:\My_Learning\Python\SolutionsAndReferences\Excel Consolidation\Consolidating Workbooks\*.xlsx', recursive = False)

# Empty dataframe
consolidated_data = pd.DataFrame()

for file in files:

    # Reading Excel data
    read_data = pd.read_excel(file)

    # Load the data into Dataframe
    consolidated_data = pd.concat([consolidated_data, read_data], ignore_index = True)

# Writing the data into Excel File

consolidated_data.to_excel(r"D:\My_Learning\Python\SolutionsAndReferences\Excel Consolidation\Consolidating Workbooks\Consolidation.xlsx", 'Consolidated', index = False)

# Completion Status
print("Completed!!!!")