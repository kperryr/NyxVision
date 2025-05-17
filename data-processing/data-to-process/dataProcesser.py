import json
import os

#Folder path with data to process
path = r"C:\Users\kpola\CodeProjects\NyxVision\data-processing\data-to-process"

#change path
os.chdir(path)

def readJSONfile(filePath):
    with open(filePath,'r') as f:
        print(f.read())

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".json"):
        file_path = f"{path}\{file}"

        # call read text file function
        readJSONfile(file_path)


        
