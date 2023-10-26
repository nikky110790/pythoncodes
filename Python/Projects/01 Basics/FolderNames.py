# Getting the folder names

# import the required libraries
import os
import glob

class List_Files_From_Folder:

    # Initialize the dictionary
    def __init__(self) -> None:
        self.file_list = {}

    def looping_folders(self, fol_path:str, file_extension:str='*', iterate_subfolders:bool=False):

        # Setting the folder path to iterate
        if fol_path.endswith('*'):
            fol_path = fol_path
        else:
            if fol_path.endswith('\\'):
                fol_path += '*'
            else:
                fol_path += '\\*'
        
        # Checking whether recursive folders has to be iterated
        folders = glob.glob(fol_path)

        for fol in folders:
            if os.path.isdir(fol):
                # folder_list.append(fol)

                # Fetching the files inside the folder path
                self.file_list[fol] = self.fetching_files_from_folder(fol, file_extension)

                if iterate_subfolders:
                    self.looping_folders(fol, file_extension, True)
        
        return self.file_list

    def fetching_files_from_folder(self, folder_path:str, file_extension:str="*") -> list:

        # Iterating the folder for files
        files = [fi for fi in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, fi)) and (file_extension == '*' or file_extension in fi.lower())]

        return files

# folder name
folder_path = r'D:\Movies\\'

# Initilizing the class
files_conso = List_Files_From_Folder()
files_conso.looping_folders(folder_path, 'mkv', True)

for directory, files in files_conso.file_list.items():

    if len(files) == 0:
        print('The directory "{0}" does not contain any files in it.'.format(directory))
    else:
        print('The directory "{0}" contains the below files in it'.format(directory))
        for file in files:
            # if '.mkv' in file.lower():
                print(file)
