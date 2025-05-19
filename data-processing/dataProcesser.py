import json
import os
import shutil
from analytics import *
from enrichmentData import *
from updateFileID import getCount

#Folder path with data to process
path = r"C:\\Users\\kpola\\CodeProjects\\NyxVision\\data-processing\\data-to-process"
oldFileDest = r"C:\\Users\\kpola\\codeProjects\\NyxVision\\data-processing\\processed-data\\oldProcessedData"

count = getCount()
#change path
os.chdir(path)

#reads JSON file and put data into an array and passes it into a function to scan the data
def readJSONfile(filePath):
    with open(filePath,'r') as f:
        #puts json data into a an arr to maniuplate
        arr = json.load(f)
        return arr
        

# iterate through all files
for file in os.listdir():
    # Check whether file is in json format or not
    if file.endswith(".json"):
        file_path = f"{path}\\{file}"

        # call read text file function
        arrReport = readJSONfile(file_path)

        for item in arrReport:
            if type(item) is dict:
                
                dataDict = scanThreatData(item)
                print(dataDict)
                processedData = combineProcessedData(dataDict["score"], dataDict["keywords"])
                item["processedData"] = processedData

                filenamePath = "C:\\Users\\kpola\\codeProjects\\NyxVision\\data-processing\\processed-data\\databaseReady\\DBDataInWaiting"+ str(count) + '.json'
                with open(filenamePath,'x') as newfile:
                    try:
                        json.dump(item,newfile,indent=4)
                        count += 1
                    except:
                        print("Please update count")
                        
        dst_path = os.path.join(oldFileDest, file)
        shutil.move(file_path, dst_path )
        

    

                








        
