import json
import os
import shutil
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from analytics import *
from enrichmentData import *
from jsonToParquet import transformToParquet

#Folder path with data to process
path = r"C:\\Users\\kpola\\CodeProjects\\NyxVision\\data-processing\\data-to-process"
oldFileDest = r"C:\\Users\\kpola\\codeProjects\\NyxVision\\data-processing\\processed-data\\oldProcessedData"


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
                processedData = combineProcessedData(item,dataDict["score"], dataDict["keywords"])
                transformToParquet(processedData)
     
        dst_path = os.path.join(oldFileDest, file)
        shutil.move(file_path, dst_path )
        

    

                








        
