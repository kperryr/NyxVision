import json
from datetime import datetime

def combineProcessedData(score, keywordArr):
    processedDict = {}
    processedDict["processedScore"] = score
    processedDict["processedKeywords"] = keywordArr
    processedDict["processedDate"] = datetime.utcnow().isoformat() + "Z"

    return processedDict

