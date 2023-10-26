import os

folderpath = r'D:\Movies'

for root, subdirectories, files in os.walk(folderpath):
    for subdirectory in subdirectories:
        print(os.path.join(root, subdirectory))
        for file in files:
            print(os.path.join(root, file))
