
import os

def getCount():
    fileDest = "C:\\Users\\kpola\\codeProjects\\NyxVision\\data-processing\\processed-data\\dataBaseReady"
    count = 0
    #change path
    os.chdir(fileDest)
    if len(os.listdir(fileDest)) == 0:
        count = 1
    else:
        for file in os.listdir():
            count += 1
        
    return count