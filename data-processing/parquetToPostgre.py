import pandas as pd
import os
import shutil
import json
import io
import sys
import numpy as np
#from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import TIMESTAMP
import traceback



try:
    input_stream = sys.stdin.buffer.read()
    log_path = r"C:\\Users\\kpola\\codeProjects\\NyxVision\\data-processing\\nifi_debug_log.txt"
    error_log_path = r"C:\\Users\\kpola\\codeProjects\\NyxVision\\data-processing\\nifi_error_log.txt"

    #set up .env later
    #load_dotenv()
    #database_url = os.getenv("postgresql://postgres:[YOUR-PASSWORD]@db.aopnzuzktznquepirstb.supabase.co:5432/postgres")
    with open(log_path, "a") as log:
        log.write(f"Reading file: {io.BytesIO(input_stream)}\n")

    
    # Read Parquet
    df = pd.read_parquet(io.BytesIO(input_stream))

    df.set_index('reportId', inplace=True)

    if 'coordinates' in df.columns: 
        df['coordinates'] = df['coordinates'].apply(lambda x: list(x) if isinstance(x, (list, np.ndarray)) else [])

    if 'keywords' in df.columns:
        df['keywords'] = df['keywords'].apply(lambda x: x.tolist() if isinstance(x, (list, np.ndarray)) else [])

    if 'processedKeywords' in df.columns:
        df['processedKeywords'] = df['processedKeywords'].apply(lambda x: x if isinstance(x, dict) else {})

    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True, errors='coerce')

    # Connect to PostgreSQL
    engine = create_engine("postgresql+psycopg2://postgres.aopnzuzktznquepirstb:kQMXEDfmokoaguVr@aws-0-us-east-2.pooler.supabase.com:5432/postgres", pool_size=5,
    max_overflow=0)

    # Write to PostgreSQL
    df.to_sql('intel_reports', 
            engine, 
            if_exists='append', 
            index= True,
            index_label='reportId',
            dtype={
                'coordinates':JSONB,
                'keywords': JSONB,
                'processedKeywords': JSONB,
                'timestamp':TIMESTAMP(timezone=True),
                'processedDate':TIMESTAMP(timezone=True)

            }
    )

    #src_path = os.path.join(path, file)
    #dest_path = os.path.join(dst_path, file)
    #shutil.move(src_path, dest_path) 

    with open(log_path, "a") as log:
        log.write(f"Successfully inserted {len(df)} records.\n")

except Exception as e:
    with open("nifi_error_log.txt", "w") as f:
        f.write("Script crashed!\n")
        f.write(str(e))
        f.write("\n")
        f.write(traceback.format_exc())
    raise

