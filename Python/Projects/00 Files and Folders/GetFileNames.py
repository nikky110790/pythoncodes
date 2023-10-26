# import required module
import os
import csv
 
# function to save the list to a csv file
def Convert_List_To_CSV(header:list
                        , records:list
                        , file_path:str):

    # creating a csv file and saving the list values inside it
    with open(file_path, 'w') as f:
        
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        # writing the csv header
        write.writerow(header)

        # writing the csv records
        write.writerows(records)

# function to read the folders and files inside it
def Read_Folder_Path(folder_path:str) -> dict:

    # initializing the list of file names
    file_names = {}

    # initializing the folder path
    folder = folder_path

    # initializing the file list
    files = []

    # Reading the folder path to get the files inside it
    dir_list = os.listdir(folder_path)

    # prints all files
    for file in dir_list:

        # full path
        full_path = folder_path + '\\' + file

        # checking if the path is file
        if os.path.isfile(full_path):
            files.append(file)
    
    # updating the dictionary
    file_names.update({folder : files})

    # returning the dict
    return file_names

# function to read the folder path and get the files inside it
# def file_names_to_csv()

# folder to read the files inside it
# Get the list of all files and directories
path = r"D:\Wedding And Reception\Selections"

files_folders = Read_Folder_Path(path)

print(files_folders)



