import json
from datetime import datetime

def combineProcessedData(dict, score, keywordArr):
    
    dict["processedScore"] = score

    dict["processedKeywords"] = keywordArr if keywordArr else None
    dict["processedDate"] = datetime.utcnow().isoformat() + "Z"

    return dict

