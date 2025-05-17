import json
import os

#Folder path with data to process
path = r"C:\Users\kpola\CodeProjects\NyxVision\data-processing\data-to-process"

#change path
os.chdir(path)

#reads JSON file and put data into an array and passes it into a function to scan the data
def readJSONfile(filePath):
    with open(filePath,'r') as f:
        #puts json data into a an arr to maniuplate
        arr = json.load(f)
        

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".json"):
        file_path = f"{path}\\{file}"

        # call read text file function
        readJSONfile(file_path)

#create loop for each item in arr
    #pass into scanning funcs
    #get data and create enrichment json to odd to OG json report
"""        
        add:
            keyword array
            score
            date processed
 """



        
