import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from updateFileID import *

def transformToParquet(jsonData):
    count = getCount()
    df = pd.DataFrame([jsonData])

    # Convert DataFrame to Arrow Table
    table = pa.Table.from_pandas(df)

    filenamePath = "C:\\Users\\kpola\\codeProjects\\NyxVision\\data-processing\\processed-data\\databaseReady\\DBDataInWaiting"+ str(count) + '.parquet'
    flag = False
    while not flag:
        if not os.path.exists(filenamePath):
            pq.write_table(table, filenamePath)
            count += 1
            flag = True
        else:
            print("File already exists. Update the count.")
            count = getCount()

    