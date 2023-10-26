# Consolidating worksheets with same columns but in different order
# Importing requried libraries
import pandas as pd
import glob

# Arguments to be passed to import excel and consolidate it
# File path
file_path = r"D:\My_Learning\Python\SolutionsAndReferences\Excel Consolidation\Consolidating Different Order columns\SampleData_V1.0.xlsx"

# Rows to skip from start
rows_to_skip = 1

# Setting the file object
file = glob.glob(file_path)

# Creating a dummy data frame
sheets_data = pd.DataFrame()

# Creating a dictionary to store the sheets and values in it
all_sheets_data = pd.read_excel(file_path, sheet_name=None, skiprows = rows_to_skip)

for name, data in all_sheets_data.items():

    sheets_data = pd.concat([sheets_data, data])
    # break

# Writing the data back to excel file
sheets_data.to_excel(r'D:\My_Learning\Python\SolutionsAndReferences\Excel Consolidation\Consolidating Different Order columns\Consolidated_Data.xlsx', index = False)

sheets_data.to_string(r'D:\My_Learning\Python\SolutionsAndReferences\Excel Consolidation\Consolidating Different Order columns\Text.txt', index=False)

# sheets_data.to_json(r'D:\My_Learning\Python\SolutionsAndReferences\Excel Consolidation\Consolidating Different Order columns\Json_File.json')

# Completion message
print('Consolidated data prepared!!!!!')