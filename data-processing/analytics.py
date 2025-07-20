import json
import yaml
import os
from config.getKeywords import *


threatKeys = getThreatKeywords()

        

#Methods to scan JSON array


 #Scan josn for words/phrases
def scanThreatData(reportDict):
    #reset score and  each new func call
    score = 0
    dictKeywordCount = {}
    
    threatKeys = getThreatKeywords()
    textToScan = reportDict["fullText"]
    
    if(textToScan is None): #fix
        return ["No summary to scan"]
    
    for category in threatKeys.values():
        for keyword, weight in category.items():
             threatCount = textToScan.count(keyword)
             if threatCount > 0:
                dictKeywordCount[keyword] = threatCount
             score += threatCount * weight
    return {"keywords":scanNegation(textToScan,score, dictKeywordCount),"score": score}

def scanNegation(text,score, dict):
    negation = getNegationKeywords()
    if(text is None):
        return
    
    for category in negation.values():
        for keyword, weight in category.items():
            negationCount = text.count(keyword)
            if negationCount > 0:
                for key in dict: #fix so that way dupilcaties are handled but for right now this is fine
                    if key in keyword:
                        if dict[key] > 0:
                            dict[key] -=1
                        else:
                            del dict[key]
                score -= negationCount * weight
    
    return dict